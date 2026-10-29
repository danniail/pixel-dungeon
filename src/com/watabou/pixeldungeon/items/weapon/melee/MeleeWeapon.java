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
package com.watabou.pixeldungeon.items.weapon.melee;

import com.watabou.pixeldungeon.Dungeon;
import com.watabou.pixeldungeon.items.Item;
import com.watabou.pixeldungeon.items.weapon.Weapon;
import com.watabou.pixeldungeon.utils.Utils;
import com.watabou.utils.Random;

public class MeleeWeapon extends Weapon {
	
	private int tier;
	
	public MeleeWeapon( int tier, float acu, float dly ) {
		super();
		
		this.tier = tier;
		
		ACU = acu;
		DLY = dly;
		
		STR = typicalSTR();
	}
	
	protected int min0() {
		return tier;
	}
	
	protected int max0() {
		return (int)((tier * tier - tier + 10) / ACU * DLY);
	}
	
	@Override
	public int min() {
		return isBroken() ? min0() : min0() + level(); 
	}
	
	@Override
	public int max() {
		return isBroken() ? max0() : max0() + level() * tier;
	}
	
	@Override
	final public Item upgrade() {
		return upgrade( false );
	}
	
	public Item upgrade( boolean enchant ) {
		STR--;		
		return super.upgrade( enchant );
	}
	
	public Item safeUpgrade() {
		return upgrade( enchantment != null );
	}
	
	@Override
	public Item degrade() {		
		STR++;
		return super.degrade();
	}
	
	public int typicalSTR() {
		return 8 + tier * 2;
	}
	
	@Override
	public String info() {

		final String p = "\n\n";

		StringBuilder info = new StringBuilder( desc() );

		int lvl = visiblyUpgraded();
		String quality = lvl != 0 ?
			(lvl > 0 ?
				(isBroken() ? "损坏" : "强化") :
				"退化") :
			"";
		info.append( p );
		info.append( "这把" + name + "是" + (quality.length() > 0 ? "一件" + quality + "的" : "一件") );
		info.append( tier + "阶近战兵器。" );

		if (levelKnown) {
			int min = min();
			int max = max();
			info.append( "它每次命中的平均伤害为" + (min + (max - min) / 2) + "点。" );
		} else {
			int min = min0();
			int max = max0();
			info.append(
				"它通常每次命中的平均伤害为" + (min + (max - min) / 2) + "点，" +
				"一般需要" + typicalSTR() + "点力道。" );
			if (typicalSTR() > Dungeon.hero.STR()) {
				info.append( "这把兵器对你来说可能太重了。" );
			}
		}

		if (DLY != 1f) {
			info.append( "这是一把相当" + (DLY < 1f ? "快速" : "缓慢") );
			if (ACU != 1f) {
				if ((ACU > 1f) == (DLY < 1f)) {
					info.append( "且");
				} else {
					info.append( "但");
				}
				info.append( ACU > 1f ? "精准" : "失准" );
			}
			info.append( "的兵器。");
		} else if (ACU != 1f) {
			info.append( "这是一把相当" + (ACU > 1f ? "精准" : "失准") + "的兵器。" );
		}
		switch (imbue) {
		case SPEED:
			info.append( "它经过调整以提升速度。" );
			break;
		case ACCURACY:
			info.append( "它经过调整以提升精准度。" );
			break;
		case NONE:
		}

		if (enchantment != null) {
			info.append( "它带有祭炼。" );
		}

		if (levelKnown && Dungeon.hero.belongings.backpack.items.contains( this )) {
			if (STR > Dungeon.hero.STR()) {
				info.append( p );
				info.append(
					"由于你的力道不足，使用这把" + name +
					"攻击的精准度和速度都下降了。" );
			}
			if (STR < Dungeon.hero.STR()) {
				info.append( p );
				info.append(
					"由于你的力道富余，使用这把" + name +
					"攻击的伤害提升了。" );
			}
		}

		if (isEquipped( Dungeon.hero )) {
			info.append( p );
			info.append( "你手持" + name + "，随时准备出击" +
				(cursed ? "，但由于它被煞气禁制，你无法将它放下。" : "。") );
		} else {
			if (cursedKnown && cursed) {
				info.append( p );
				info.append( "你能感觉到" + name + "中潜藏着邪异的灵力。" );
			}
		}

		return info.toString();
	}
	
	@Override
	public int price() {
		int price = 20 * (1 << (tier - 1));
		if (enchantment != null) {
			price *= 1.5;
		}
		return considerState( price );
	}
	
	@Override
	public Item random() {
		super.random();
		
		if (Random.Int( 10 + level() ) == 0) {
			enchant();
		}
		
		return this;
	}
}
