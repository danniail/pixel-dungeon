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
package com.watabou.pixeldungeon.items.scrolls;

import com.watabou.noosa.audio.Sample;
import com.watabou.pixeldungeon.Assets;
import com.watabou.pixeldungeon.Dungeon;
import com.watabou.pixeldungeon.actors.buffs.Buff;
import com.watabou.pixeldungeon.actors.buffs.Invisibility;
import com.watabou.pixeldungeon.actors.buffs.Sleep;
import com.watabou.pixeldungeon.actors.mobs.Mob;
import com.watabou.pixeldungeon.effects.Speck;
import com.watabou.pixeldungeon.levels.Level;
import com.watabou.pixeldungeon.utils.GLog;

public class ScrollOfLullaby extends Scroll {

	{
		name = "安魂符";
	}
	
	@Override
	protected void doRead() {
		
		curUser.sprite.centerEmitter().start( Speck.factory( Speck.NOTE ), 0.3f, 5 );
		Sample.INSTANCE.play( Assets.SND_LULLABY );
		Invisibility.dispel();
		
		int count = 0;
		Mob affected = null;
		for (Mob mob : Dungeon.level.mobs.toArray( new Mob[0] )) {
			if (Level.fieldOfView[mob.pos]) {
				Buff.affect( mob, Sleep.class );
				if (mob.buff( Sleep.class ) != null) {
					affected = mob;
					count++;
				}
			}
		}
		
		switch (count) {
		case 0:
			GLog.i( "符箓奏出舒缓的旋律。" );
			break;
		case 1:
			GLog.i( "符箓奏出舒缓的旋律，" + affected.name + "睡着了！" );
			break;
		default:
			GLog.i( "符箓奏出舒缓的旋律，妖兽们睡着了！" );
		}
		setKnown();
		
		readAnimation();
	}
	
	@Override
	public String desc() {
		return "舒缓的旋律会让你视野内的所有生物陷入沉睡，让你有机会逃跑或发动突袭。";
	}
	
	@Override
	public int price() {
		return isKnown() ? 50 * quantity : super.price();
	}
}
