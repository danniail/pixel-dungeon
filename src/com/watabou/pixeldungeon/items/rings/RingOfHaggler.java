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
package com.watabou.pixeldungeon.items.rings;

import com.watabou.pixeldungeon.Badges;
import com.watabou.pixeldungeon.actors.hero.Hero;
import com.watabou.pixeldungeon.items.Item;

public class RingOfHaggler extends Ring {

	{
		name = "商贾戒";
	}
	
	@Override
	protected RingBuff buff( ) {
		return new Haggling();
	}
	
	@Override
	public Item random() {
		level( +1 );
		return this;
	}
	
	@Override
	public boolean doPickUp( Hero hero ) {
		identify();
		Badges.validateRingOfHaggler();
		Badges.validateItemLevelAquired( this );
		return super.doPickUp(hero);
	}
	
	@Override
	public boolean isUpgradable() {
		return false;
	}
	
	@Override
	public void use() {
		// Do nothing (it can't degrade)
	}
	
	@Override
	public String desc() {
		return isKnown() ?
			"这枚法宝本身并无其他妙用，却能向坊市中的店主和商贩表明，" +
			"持戒者是散修盟中的人物。他们通常乐意给个折扣，以换取" +
			"一时的平安。强化这枚法宝不会带来额外好处。" :
			super.desc();
	}
	
	public class Haggling extends RingBuff {	
	}
}
