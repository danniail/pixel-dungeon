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
package com.watabou.pixeldungeon.items.armor;

import com.watabou.noosa.audio.Sample;
import com.watabou.pixeldungeon.Assets;
import com.watabou.pixeldungeon.Dungeon;
import com.watabou.pixeldungeon.actors.Actor;
import com.watabou.pixeldungeon.actors.buffs.Buff;
import com.watabou.pixeldungeon.actors.buffs.Burning;
import com.watabou.pixeldungeon.actors.buffs.Roots;
import com.watabou.pixeldungeon.actors.hero.Hero;
import com.watabou.pixeldungeon.actors.hero.HeroClass;
import com.watabou.pixeldungeon.actors.mobs.Mob;
import com.watabou.pixeldungeon.effects.particles.ElmoParticle;
import com.watabou.pixeldungeon.levels.Level;
import com.watabou.pixeldungeon.sprites.ItemSpriteSheet;
import com.watabou.pixeldungeon.utils.GLog;

public class MageArmor extends ClassArmor {	
	
	private static final String AC_SPECIAL = "焚天烈焰"; 
	
	private static final String TXT_NOT_MAGE	= "只有修仙者能使用这件法袍！";
	
	{
		name = "修仙道袍";
		image = ItemSpriteSheet.ARMOR_MAGE;
	}
	
	@Override
	public String special() {
		return AC_SPECIAL;
	}
	
	@Override
	public String desc() {
		return "穿上这件灵光流转的道袍，修仙者可施展焚天烈焰：视野内所有敌人都会被点燃，同时周身如被灵藤缠绕，无法移动。";
	}
	
	@Override
	public void doSpecial() {	

		for (Mob mob : Dungeon.level.mobs) {
			if (Level.fieldOfView[mob.pos]) {
				Buff.affect( mob, Burning.class ).reignite( mob );
				Buff.prolong( mob, Roots.class, 3 );
			}
		}
		
		curUser.HP -= (curUser.HP / 3);
		
		curUser.spend( Actor.TICK );
		curUser.sprite.operate( curUser.pos );
		curUser.busy();
		
		curUser.sprite.centerEmitter().start( ElmoParticle.FACTORY, 0.15f, 4 );
		Sample.INSTANCE.play( Assets.SND_READ );
	}
	
	@Override
	public boolean doEquip( Hero hero ) {
		if (hero.heroClass == HeroClass.MAGE) {
			return super.doEquip( hero );
		} else {
			GLog.w( TXT_NOT_MAGE );
			return false;
		}
	}
}