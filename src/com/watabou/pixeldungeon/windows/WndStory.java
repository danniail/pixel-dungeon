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
package com.watabou.pixeldungeon.windows;

import com.watabou.input.Touchscreen.Touch;
import com.watabou.noosa.BitmapTextMultiline;
import com.watabou.noosa.Game;
import com.watabou.noosa.TouchArea;
import com.watabou.pixeldungeon.Chrome;
import com.watabou.pixeldungeon.Dungeon;
import com.watabou.pixeldungeon.scenes.PixelScene;
import com.watabou.pixeldungeon.ui.Window;
import com.watabou.utils.SparseArray;

public class WndStory extends Window {

	private static final int WIDTH = 120;
	private static final int MARGIN = 6;
	
	private static final float bgR	= 0.77f;
	private static final float bgG	= 0.73f;
	private static final float bgB	= 0.62f;
	
	public static final int ID_SEWERS		= 0;
	public static final int ID_PRISON		= 1;
	public static final int ID_CAVES		= 2;
	public static final int ID_METROPOLIS	= 3;
	public static final int ID_HALLS		= 4;
	
	private static final SparseArray<String> CHAPTERS = new SparseArray<String>();
	
	static {
		CHAPTERS.put( ID_SEWERS, 
		"地牢就在城市正下方，它的上层实际上构成了城市的下水道系统。" +
		"名义上属于城市，这些层并不那么危险。没人会说这是个安全的地方，" +
		"但至少你不必在这里对付邪恶魔法。" );
		
		CHAPTERS.put( ID_PRISON, 
		"许多年前，这里建了一座地下监狱，关押最危险的罪犯。当时这" +
		"看起来是个绝妙的主意，因为这里确实很难逃脱。但很快，黑暗的瘴气开始渗出，" +
		"让囚犯和守卫发疯。最终监狱被废弃，尽管有些囚犯" +
		"还被锁在这里。" );
		
		CHAPTERS.put( ID_CAVES, 
		"废弃监狱下方延伸的洞穴人烟稀少。它们太深，城市无法开采；" +
		"矿物又太贫乏，矮人不感兴趣。过去，在这条商路上" +
		"曾有一个贸易前哨站，但自矮人城邦衰落以来，它也消亡了。" +
		"如今只有无处不在的豺狼和地下动物栖息于此。" );
		
		CHAPTERS.put( ID_METROPOLIS, 
		"矮人城邦曾是最伟大的矮人城邦。鼎盛时期，矮人的机械化军队" +
		"成功击退了古神和他的恶魔大军的入侵。但据说，归来的战士" +
		"带回了腐败的种子，那场胜利正是这个地下王国走向终结的开端。" );
		
		CHAPTERS.put( ID_HALLS,
		"过去这些层是城邦的郊区。在与古神的战争中付出惨重代价后，" +
		"矮人太过虚弱，无法清除残余的恶魔。恶魔逐渐收紧了对这里的控制，" +
		"如今这里被称为恶魔大厅。\n\n" +
		"极少有冒险者能走到这么远……" );
	};
	
	private BitmapTextMultiline tf;
	
	private float delay;
	
	public WndStory( String text ) {
		super( 0, 0, Chrome.get( Chrome.Type.SCROLL ) );
		
		tf = PixelScene.createMultiline( text, 7 );
		tf.maxWidth = WIDTH - MARGIN * 2;
		tf.measure();
		tf.ra = bgR;
		tf.ga = bgG;
		tf.ba = bgB;
		tf.rm = -bgR;
		tf.gm = -bgG;
		tf.bm = -bgB;
		tf.x = MARGIN;
		add( tf );
		
		add( new TouchArea( chrome ) {
			@Override
			protected void onClick( Touch touch ) {
				hide();
			}
		} );
		
		resize( (int)(tf.width() + MARGIN * 2), (int)Math.min( tf.height(), 180 ) );
	}
	
	@Override
	public void update() {
		super.update();
		
		if (delay > 0 && (delay -= Game.elapsed) <= 0) {
			shadow.visible = chrome.visible = tf.visible = true;
		}
	}
	
	public static void showChapter( int id ) {
		
		if (Dungeon.chapters.contains( id )) {
			return;
		}
		
		String text = CHAPTERS.get( id );
		if (text != null) {
			WndStory wnd = new WndStory( text );
			if ((wnd.delay = 0.6f) > 0) {
				wnd.shadow.visible = wnd.chrome.visible = wnd.tf.visible = false;
			}
			
			Game.scene().add( wnd );
			
			Dungeon.chapters.add( id );
		}
	}
}
