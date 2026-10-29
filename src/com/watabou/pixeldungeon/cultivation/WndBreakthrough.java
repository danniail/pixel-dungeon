/*
 * One-shot Foundation Establishment breakthrough presentation.
 */
package com.watabou.pixeldungeon.cultivation;

import com.watabou.noosa.BitmapTextMultiline;
import com.watabou.pixeldungeon.scenes.GameScene;
import com.watabou.pixeldungeon.scenes.PixelScene;
import com.watabou.pixeldungeon.ui.RedButton;
import com.watabou.pixeldungeon.ui.Window;

public class WndBreakthrough extends Window {

	private static final int WIDTH = 132;
	private static final int BUTTON_HEIGHT = 20;
	private static final int GAP = 4;

	private final boolean success;

	public WndBreakthrough() {
		this( false );
	}

	private WndBreakthrough( boolean success ) {
		super();
		this.success = success;

		BitmapTextMultiline text = PixelScene.createMultiline( success ?
			"筑基成功！\n\n你的气息已与天地灵气相合，真元上限提升至10点，气血完全恢复。\n\n" +
			"此刻可参悟一门主动功法：青云剑诀。" :
			"炼气圆满，筑基在望。\n\n引动秘境灵气冲击筑基瓶颈。突破后将开启真元，" +
			"并获得一次功法参悟机会。", 7 );
		text.maxWidth = WIDTH;
		text.measure();
		add( text );

		RedButton button = new RedButton( success ? "参悟青云剑诀" : "引动灵气，开始筑基" ) {
			@Override
			protected void onClick() {
				hide();
				if (WndBreakthrough.this.success) {
					Cultivation.learnQingyun();
					GameScene.show( new WndTechnique() );
				} else {
					Cultivation.completeFoundation();
					GameScene.show( new WndBreakthrough( true ) );
				}
			}
		};
		button.setRect( 0, text.height() + GAP, WIDTH, BUTTON_HEIGHT );
		add( button );

		resize( WIDTH, (int)button.bottom() );
	}

	@Override
	public void onBackPressed() {
		// Keep the one-time breakthrough choice explicit.
	}
}
