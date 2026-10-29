/*
 * Pixel Dungeon
 * Copyright (C) 2012-2015 Oleg Dolya
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>
 */
package com.watabou.pixeldungeon.actors.mobs.npcs;

import com.watabou.pixeldungeon.Dungeon;
import com.watabou.pixeldungeon.Journal;
import com.watabou.pixeldungeon.actors.Actor;
import com.watabou.pixeldungeon.actors.Char;
import com.watabou.pixeldungeon.actors.buffs.Buff;
import com.watabou.pixeldungeon.actors.mobs.Golem;
import com.watabou.pixeldungeon.actors.mobs.Mob;
import com.watabou.pixeldungeon.actors.mobs.Monk;
import com.watabou.pixeldungeon.items.Generator;
import com.watabou.pixeldungeon.items.quest.DwarfToken;
import com.watabou.pixeldungeon.items.rings.Ring;
import com.watabou.pixeldungeon.levels.CityLevel;
import com.watabou.pixeldungeon.levels.Room;
import com.watabou.pixeldungeon.scenes.GameScene;
import com.watabou.pixeldungeon.sprites.ImpSprite;
import com.watabou.pixeldungeon.utils.Utils;
import com.watabou.pixeldungeon.windows.WndImp;
import com.watabou.pixeldungeon.windows.WndQuest;
import com.watabou.utils.Bundle;
import com.watabou.utils.Random;

public class Imp extends NPC {

	{
		name = "域外小魔修";
		spriteClass = ImpSprite.class;
	}
	
	private static final String TXT_GOLEMS1	=
		"你是修士吗？我喜欢修士！你总能指望他们" +
		"去杀掉该杀的东西。对吧？当然是为了酬劳;)\n" +
		"我这边呢，需要杀掉的是 _禁制傀儡_。你看，我打算在这儿" +
		"做点小买卖，但这些蠢石头疙瘩对生意没好处！" +
		"跟游荡的花岗岩块可没法谈判，该死的！" +
		"所以拜托，杀掉……就 _6个_ 吧，酬劳就是你的。";
	
	private static final String TXT_MONKS1	=
		"你是修士吗？我喜欢修士！你总能指望他们" +
		"去杀掉该杀的东西。对吧？当然是为了酬劳;)\n" +
		"我这边呢，需要杀掉的是 _武僧傀儡_。你看，我打算在这儿" +
		"做点小买卖，但这些疯子自己什么都不买，还" +
		"会吓跑其他顾客。" +
		"所以拜托，杀掉……就 _8个_ 吧，酬劳就是你的。";
	
	private static final String TXT_GOLEMS2	=
		"你的禁制傀儡杀得如何了？";	
	
	private static final String TXT_MONKS2	=
		"哦，你还活着！我就知道你功夫更厉害;) " +
		"别忘了拿这些武僧傀儡的信物。";	
	
	private static final String TXT_CYA	= "再见，%s！";
	private static final String TXT_HEY	= "嘘，%s！";
	
	private boolean seenBefore = false;
	
	@Override
	protected boolean act() {
		
		if (!Quest.given && Dungeon.visible[pos]) {
			if (!seenBefore) {
				yell( Utils.format( TXT_HEY, Dungeon.hero.className() ) );
			}
			seenBefore = true;
		} else {
			seenBefore = false;
		}
		
		throwItem();
		
		return super.act();
	}
	
	@Override
	public int defenseSkill( Char enemy ) {
		return 1000;
	}
	
	@Override
	public String defenseVerb() {
		return "闪避";
	}
	
	@Override
	public void damage( int dmg, Object src ) {
	}
	
	@Override
	public void add( Buff buff ) {
	}
	
	@Override
	public boolean reset() {
		return true;
	}
	
	@Override
	public void interact() {
		
		sprite.turnTo( pos, Dungeon.hero.pos );
		if (Quest.given) {
			
			DwarfToken tokens = Dungeon.hero.belongings.getItem( DwarfToken.class );
			if (tokens != null && (tokens.quantity() >= 8 || (!Quest.alternative && tokens.quantity() >= 6))) {
				GameScene.show( new WndImp( this, tokens ) );
			} else {
				tell( Quest.alternative ? TXT_MONKS2 : TXT_GOLEMS2, Dungeon.hero.className() );
			}
			
		} else {
			tell( Quest.alternative ? TXT_MONKS1 : TXT_GOLEMS1 );
			Quest.given = true;
			Quest.completed = false;
			
			Journal.add( Journal.Feature.IMP );
		}
	}
	
	private void tell( String format, Object...args ) {
		GameScene.show( 
			new WndQuest( this, Utils.format( format, args ) ) );
	}
	
	public void flee() {
		
		yell( Utils.format( TXT_CYA, Dungeon.hero.className() ) );
		
		destroy();
		sprite.die();
	}
	
	@Override
	public String description() {
		return 
			"小魔修是低等魔物，既不以力量著称，也不以法术天赋闻名，" +
			"但相当聪明、善于交际。许多小魔修喜欢生活在非魔物之中。";
	}
	
	public static class Quest {
		
		private static boolean alternative;
		
		private static boolean spawned;
		private static boolean given;
		private static boolean completed;
		
		public static Ring reward;
		
		public static void reset() {
			spawned = false;

			reward = null;
		}
		
		private static final String NODE		= "demon";
		
		private static final String ALTERNATIVE	= "alternative";
		private static final String SPAWNED		= "spawned";
		private static final String GIVEN		= "given";
		private static final String COMPLETED	= "completed";
		private static final String REWARD		= "reward";
		
		public static void storeInBundle( Bundle bundle ) {
			
			Bundle node = new Bundle();
			
			node.put( SPAWNED, spawned );
			
			if (spawned) {
				node.put( ALTERNATIVE, alternative );
				
				node.put( GIVEN, given );
				node.put( COMPLETED, completed );
				node.put( REWARD, reward );
			}
			
			bundle.put( NODE, node );
		}
		
		public static void restoreFromBundle( Bundle bundle ) {

			Bundle node = bundle.getBundle( NODE );
			
			if (!node.isNull() && (spawned = node.getBoolean( SPAWNED ))) {
				alternative	= node.getBoolean( ALTERNATIVE );
				
				given = node.getBoolean( GIVEN );
				completed = node.getBoolean( COMPLETED );
				reward = (Ring)node.get( REWARD );
			}
		}
		
		public static void spawn( CityLevel level, Room room ) {
			if (!spawned && Dungeon.depth > 16 && Random.Int( 20 - Dungeon.depth ) == 0) {
				
				Imp npc = new Imp();
				do {
					npc.pos = level.randomRespawnCell();
				} while (npc.pos == -1 || level.heaps.get( npc.pos ) != null);
				level.mobs.add( npc );
				Actor.occupyCell( npc );
				
				spawned = true;	
				alternative = Random.Int( 2 ) == 0;
				
				given = false;
				
				do {
					reward = (Ring)Generator.random( Generator.Category.RING );
				} while (reward.cursed);
				reward.upgrade( 2 );
				reward.cursed = true;
			}
		}
		
		public static void process( Mob mob ) {
			if (spawned && given && !completed) {
				if ((alternative && mob instanceof Monk) ||
					(!alternative && mob instanceof Golem)) {
					
					Dungeon.level.drop( new DwarfToken(), mob.pos ).sprite.drop();
				}
			}
		}
		
		public static void complete() {
			reward = null;
			completed = true;
			
			Journal.remove( Journal.Feature.IMP );
		}
		
		public static boolean isCompleted() {
			return completed;
		}
	}
}
