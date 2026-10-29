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
import com.watabou.pixeldungeon.actors.buffs.Terror;
import com.watabou.pixeldungeon.actors.mobs.Mob;
import com.watabou.pixeldungeon.effects.Flare;
import com.watabou.pixeldungeon.levels.Level;
import com.watabou.pixeldungeon.utils.GLog;

public class ScrollOfTerror extends Scroll {

	{
		name = "慑魂符";
	}
	
	@Override
	protected void doRead() {
		
		new Flare( 5, 32 ).color( 0xFF0000, true ).show( curUser.sprite, 2f );
		Sample.INSTANCE.play( Assets.SND_READ );
		Invisibility.dispel();
		
		int count = 0;
		Mob affected = null;
		for (Mob mob : Dungeon.level.mobs.toArray( new Mob[0] )) {
			if (Level.fieldOfView[mob.pos]) {
				Buff.affect( mob, Terror.class, Terror.DURATION ).object = curUser.id();
				
				count++;
				affected = mob;
			}
		}
		
		switch (count) {
		case 0:
			GLog.i( "符箓发出一道耀眼的红光" );
			break;
		case 1:
			GLog.i( "符箓发出一道耀眼的红光，" + affected.name + "逃跑了！" );
			break;
		default:
			GLog.i( "符箓发出一道耀眼的红光，妖兽们逃跑了！" );
		}
		setKnown();
		
		readAnimation();
	}
	
	@Override
	public String desc() {
		return "一道红光会让你视野内的所有生物陷入恐惧，转身逃跑。攻击逃跑的敌人会解除效果。";
	}
	
	@Override
	public int price() {
		return isKnown() ? 50 * quantity : super.price();
	}
}
