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
		"你踏入废弃药园。这里曾是上古修士栽种灵草的药圃，" +
		"如今水渠淤塞、灵田荒芜，噬灵鼠与低阶妖兽在残存的药香中出没。" +
		"外围禁制虽已残破，仍不可轻敌。" );

		CHAPTERS.put( ID_PRISON,
		"穿过药园，便来到古修洞府。这里曾封印凶妖与魔修，" +
		"禁制石柱和傀儡守卫至今仍在运转。岁月使封印松动，" +
		"被困的凶物正等待新的血食。" );

		CHAPTERS.put( ID_CAVES,
		"洞府之下，是地火矿脉。岩浆映照着废弃矿道，" +
		"地火与灵气交织，催生出凶猛妖物。矿脉深处仍藏着灵矿与古修遗宝，" +
		"但每一步都可能惊醒沉睡的机关。" );

		CHAPTERS.put( ID_METROPOLIS,
		"矿脉尽头，是失落仙城。这里曾是洞府主人与门下修士居住之地，" +
		"如今只剩残垣、禁制和傀儡大军。域外天魔留下的侵蚀，" +
		"仍在这座古城的阴影中蔓延。" );

		CHAPTERS.put( ID_HALLS,
		"仙城之后，便是天魔殿。这里本是洞府主人的闭关之所，" +
		"如今天魔残念盘踞，禁地与魔气融为一体。飞升仙宝就在殿宇最深处，" +
		"而域外天魔正等待最后的闯入者。" );

		CHAPTERS.put( 11,
		"废弃药园深处的污水忽然翻涌，腐烂药草与淤泥聚成庞大身躯。" +
		"污秽妖王封锁了药园出口，唯有击败它，才能继续深入。" );

		CHAPTERS.put( 12,
		"古修洞府的封印中枢亮起幽光。曾被镇压的鸦妖王夺回双刃，" +
		"在石柱间疾行如风。它不会让任何修士带走洞府中的秘密。" );

		CHAPTERS.put( 13,
		"地火矿脉的核心传来沉重轰鸣。机关傀儡王从熔岩旁苏醒，" +
		"青铜躯壳上的古修符文逐一亮起，矿道随之封闭。" );

		CHAPTERS.put( 14,
		"失落仙城中央，傀儡之主登上残破的王座。" +
		"它仍执行着上古修士最后的命令：清除所有未经许可的入侵者。" );

		CHAPTERS.put( 15,
		"天魔殿的魔气凝成实质，域外天魔在仙宝前显形。" +
		"这是秘境最后的守关者，也是你飞升之前必须斩断的魔障。" );
	}

	public static String regionName( int depth ) {
		if (depth <= 5) {
			return "废弃药园";
		} else if (depth <= 10) {
			return "古修洞府";
		} else if (depth <= 15) {
			return "地火矿脉";
		} else if (depth <= 20) {
			return "失落仙城";
		} else if (depth <= 25) {
			return "天魔殿";
		} else {
			return "飞升仙台";
		}
	}

	public static void showBoss( int depth ) {
		if (Dungeon.bossLevel( depth )) {
			showChapter( 10 + depth / 5 );
		}
	}
	
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
