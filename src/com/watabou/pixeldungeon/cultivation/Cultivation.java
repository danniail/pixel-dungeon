/*
 * Cultivation progression, true essence recovery and the first active technique.
 */
package com.watabou.pixeldungeon.cultivation;

import java.io.IOException;

import com.watabou.noosa.audio.Sample;
import com.watabou.pixeldungeon.Assets;
import com.watabou.pixeldungeon.Dungeon;
import com.watabou.pixeldungeon.actors.Actor;
import com.watabou.pixeldungeon.actors.Char;
import com.watabou.pixeldungeon.actors.hero.Hero;
import com.watabou.pixeldungeon.effects.Flare;
import com.watabou.pixeldungeon.effects.MagicMissile;
import com.watabou.pixeldungeon.effects.Speck;
import com.watabou.pixeldungeon.scenes.GameScene;
import com.watabou.pixeldungeon.sprites.CharSprite;
import com.watabou.pixeldungeon.mechanics.Ballistica;
import com.watabou.pixeldungeon.utils.GLog;
import com.watabou.utils.Bundle;
import com.watabou.utils.Callback;
import com.watabou.utils.Random;

public class Cultivation {

	private static final String KEY = "cultivation";
	private static final int FOUNDATION_LEVEL = 10;
	private static final int QINGYUN_COST = 3;
	private static final int QINGYUN_RANGE = 6;
	private static final int RECOVERY_PERIOD = 4;

	private static CultivationState state = new CultivationState();

	public static void reset() {
		state = new CultivationState();
	}

	public static void storeInBundle( Bundle bundle ) {
		bundle.put( KEY, state );
	}

	public static void restoreFromBundle( Bundle bundle ) {
		Bundle saved = bundle.getBundle( KEY );
		if (saved.isNull()) {
			reset();
		} else {
			state = new CultivationState();
			state.restoreFromBundle( saved );
		}
	}

	public static String realmTitle( int level ) {
		return Realm.title( level );
	}

	public static String trueEssenceText() {
		return state.foundationDone ? state.trueEssence + "/" + state.maxTrueEssence() : "筑基后开启";
	}

	public static boolean isQingyunKnown() {
		return state.qingyunKnown;
	}

	public static void onLevelUp( Hero hero ) {
		if (hero.lvl >= FOUNDATION_LEVEL && !state.foundationDone) {
			state.breakthroughPending = true;
			showPendingBreakthrough();
		}
	}

	public static void showPendingBreakthrough() {
		if (state.breakthroughPending && !state.foundationDone) {
			GameScene.show( new WndBreakthrough() );
		}
	}

	public static void completeFoundation() {
		if (state.foundationDone) {
			return;
		}

		state.foundationDone = true;
		state.breakthroughPending = false;
		state.trueEssence = state.maxTrueEssence();
		state.recoveryTurns = 0;

		Hero hero = Dungeon.hero;
		hero.HP = hero.HT;
		hero.sprite.showStatus( CharSprite.POSITIVE, "筑基成功" );
		hero.sprite.emitter().burst( Speck.factory( Speck.HEALING ), 16 );
		new Flare( 8, 48 ).color( 0x66CCFF, true ).show( hero.sprite, 1.5f );
		Sample.INSTANCE.play( Assets.SND_LEVELUP );
		GLog.p( "灵气贯体，周天自成。你成功踏入筑基境界，真元已经充盈。" );
		saveQuietly();
	}

	public static void learnQingyun() {
		if (!state.foundationDone) {
			return;
		}
		state.qingyunKnown = true;
		GLog.p( "你参悟了青云剑诀。施展时消耗3点真元，可御剑攻击六格内的敌人。" );
		saveQuietly();
	}

	public static void onTurn() {
		if (!state.foundationDone || state.trueEssence >= state.maxTrueEssence()) {
			return;
		}
		state.recoveryTurns++;
		if (state.recoveryTurns >= RECOVERY_PERIOD) {
			state.recoveryTurns = 0;
			state.trueEssence = Math.min( state.trueEssence + 1, state.maxTrueEssence() );
		}
	}

	public static void castQingyun( Hero hero, int cell ) {
		if (!state.qingyunKnown) {
			GameScene.show( new WndTechnique() );
			return;
		}
		if (state.trueEssence < QINGYUN_COST) {
			GLog.w( "真元不足。青云剑诀需要3点真元，每4回合恢复1点。" );
			return;
		}

		Char enemy = Actor.findChar( cell );
		if (enemy == null || enemy == hero) {
			GLog.i( "此处没有可御剑攻击的目标。" );
			return;
		}
		if (!Dungeon.visible[cell] || Dungeon.level.distance( hero.pos, cell ) > QINGYUN_RANGE ||
			Ballistica.cast( hero.pos, cell, false, true ) != cell) {
			GLog.i( "目标不在青云剑诀的御剑范围内。" );
			return;
		}

		state.trueEssence -= QINGYUN_COST;
		state.recoveryTurns = 0;
		hero.sprite.zap( cell );
		hero.spendAndNext( 1f );
		Sample.INSTANCE.play( Assets.SND_ZAP );
		GLog.p( "你掐诀御剑，青云剑光直取%s！", enemy.name );

		MagicMissile.blueLight( hero.sprite.parent, hero.pos, cell, new Callback() {
			@Override
			public void call() {
				int damage = Random.IntRange( 6, 10 ) + Dungeon.hero.lvl / 2;
				enemy.damage( damage, Cultivation.class );
				enemy.sprite.burst( 0xFF66CCFF, 8 );
			}
		} );
	}

	private static void saveQuietly() {
		try {
			Dungeon.saveAll();
		} catch (IOException e) {
			GLog.w( "突破状态暂时未能写入存档。" );
		}
	}
}
