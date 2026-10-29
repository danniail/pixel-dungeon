/*
 * Qingyun Sword Technique information and activation.
 */
package com.watabou.pixeldungeon.cultivation;

import com.watabou.noosa.BitmapTextMultiline;
import com.watabou.pixeldungeon.Dungeon;
import com.watabou.pixeldungeon.scenes.GameScene;
import com.watabou.pixeldungeon.scenes.PixelScene;
import com.watabou.pixeldungeon.ui.RedButton;
import com.watabou.pixeldungeon.ui.Window;

public class WndTechnique extends Window {

	private static final int WIDTH = 132;
	private static final int BUTTON_HEIGHT = 20;
	private static final int GAP = 4;

	public WndTechnique() {
		super();

		boolean known = Cultivation.isQingyunKnown();
		BitmapTextMultiline text = PixelScene.createMultiline(
			"青云剑诀\n\n" +
			(known ?
				"以真元御使青云剑光，攻击六格内可见目标，造成6-10点基础伤害并随修为提升。\n\n" +
				"消耗：3点真元\n当前真元：" + Cultivation.trueEssenceText() +
				"\n恢复：每4回合恢复1点真元" :
				"主动功法尚未参悟。修为达到10级并完成筑基突破后，即可参悟青云剑诀。\n\n" +
				"法器充能不受真元影响，仍按原规则恢复。"), 7 );
		text.maxWidth = WIDTH;
		text.measure();
		add( text );

		RedButton button = new RedButton( known ? "选择御剑目标" : "返回修行" ) {
			@Override
			protected void onClick() {
				hide();
				if (known) {
					GameScene.selectCell( new QingyunSword() );
				}
			}
		};
		button.setRect( 0, text.height() + GAP, WIDTH, BUTTON_HEIGHT );
		add( button );

		resize( WIDTH, (int)button.bottom() );
	}
}
