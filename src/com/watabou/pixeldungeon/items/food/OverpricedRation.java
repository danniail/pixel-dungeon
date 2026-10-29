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
package com.watabou.pixeldungeon.items.food;

import com.watabou.pixeldungeon.actors.buffs.Hunger;
import com.watabou.pixeldungeon.sprites.ItemSpriteSheet;

public class OverpricedRation extends Food {

	{
		name = "灵谷干粮";
		image = ItemSpriteSheet.OVERPRICED;
		energy = Hunger.STARVING - Hunger.HUNGRY;
		message = "这灵谷干粮味道尚可。";
	}
	
	@Override
	public String info() {
		return "看起来和辟谷干粮一般无二，只是分量更少。";
	}
	
	@Override
	public int price() {
		return 20 * quantity;
	}
}
