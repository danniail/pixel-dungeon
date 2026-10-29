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
package com.watabou.pixeldungeon.scenes;

import com.watabou.noosa.Game;
import com.watabou.pixeldungeon.windows.WndStory;

public class IntroScene extends PixelScene {

	private static final String TEXT =
		"天地之间，有修士吞吐灵气，求长生大道。\n\n" +
		"在你之前，无数修仙者曾踏入这座上古修士遗留的秘境。有人寻得灵药" +
		"法宝、满载而归，更多人却葬身妖兽与禁制之下，再无音讯。但从没有人" +
		"能取到秘境最深处的那件仙宝——传说得之可窥长生、举霞飞升。\n\n" +
		"你出身平凡、资质平平，却凭着一股不肯认命的狠劲，一步步修到今日。" +
		"如今机缘在前，你压下心中悸动，深吸一口气。\n\n" +
		"修仙之路，本就逆天而行。是时候进去，搏一场属于自己的造化了！";
	
	@Override
	public void create() {
		super.create();
		
		add( new WndStory( TEXT ) {
			@Override
			public void hide() {
				super.hide();
				Game.switchScene( InterlevelScene.class );
			}
		} );
		
		fadeIn();
	}
}
