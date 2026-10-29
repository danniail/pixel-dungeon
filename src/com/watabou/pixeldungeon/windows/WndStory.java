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
		"秘境的最外层，是上古修士布下的外围禁制。这里灵气稀薄，只有些" +
		"低阶妖兽和废弃傀儡游荡。寻常修士在此历练，虽无大碍，却也不可掉以轻心——" +
		"多少惊才绝艳之辈，恰恰栽在了轻敌二字上。" );

		CHAPTERS.put( ID_PRISON,
		"再往里，是一座巨大的地下囚笼。上古修士曾将为祸世间的凶妖、魔修" +
		"尽数封印于此。岁月悠悠，封印松动，瘴气弥漫，那些被困的凶物至今仍在" +
		"黑暗中徘徊，眼中满是嗜血的饥渴。" );

		CHAPTERS.put( ID_CAVES,
		"囚笼之下，是一条幽深的灵矿矿脉，旁侧还开辟着荒废的药园。这里" +
		"曾有修士驻守采炼，矿洞深处依稀可见前人留下的痕迹。如今人去园空，" +
		"只剩些通灵的妖兽和虫豸盘踞其间，守护着残存的灵草与矿石。" );

		CHAPTERS.put( ID_METROPOLIS,
		"矿脉尽头，便是上古修士真正的洞府核心。传闻洞府主人当年修为通天，" +
		"曾以禁制和傀儡大军抵御过域外天魔的入侵。那场大战虽胜，洞府却也从此" +
		"衰落，只留下重重杀机，静候着不知死活的闯入者。" );

		CHAPTERS.put( ID_HALLS,
		"洞府最深处，是主人当年闭关清修之地。与天魔一战后，残余的魔气在此" +
		"盘踞，化作了最凶险的禁地。而那件引得无数修士疯狂的仙宝，也正沉睡于此。\n\n" +
		"能走到这里的，无一不是心志如铁之辈……" );
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
