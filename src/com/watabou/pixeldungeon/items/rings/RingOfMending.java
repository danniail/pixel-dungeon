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

public class RingOfMending extends Ring {
	
	{
		name = "修复之戒";
	}
	
	@Override
	protected RingBuff buff( ) {
		return new Rejuvenation();
	}
	
	@Override
	public String desc() {
		return isKnown() ?
			"这枚戒指增强身体的再生能力，让你以更快速度恢复失去的" +
			"生命值。损坏的戒指会减缓甚至停止你的自然恢复。" :
			super.desc();
	}
	
	public class Rejuvenation extends RingBuff {
	}
}
