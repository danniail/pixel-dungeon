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

public class RingOfHerbalism extends Ring {

	{
		name = "草药之戒";
	}
	
	@Override
	protected RingBuff buff( ) {
		return new Herbalism();
	}
	
	@Override
	public String desc() {
		return isKnown() ?
			"这枚戒指提升你从踩倒的草丛中采集露珠和种子的几率。" :
			super.desc();
	}
	
	public class Herbalism extends RingBuff {
	}
}
