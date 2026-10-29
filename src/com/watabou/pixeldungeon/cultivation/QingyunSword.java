/*
 * Target selection for Qingyun Sword Technique.
 */
package com.watabou.pixeldungeon.cultivation;

import com.watabou.pixeldungeon.Dungeon;
import com.watabou.pixeldungeon.scenes.CellSelector;

public class QingyunSword implements CellSelector.Listener {

	@Override
	public void onSelect( Integer cell ) {
		if (cell != null) {
			Cultivation.castQingyun( Dungeon.hero, cell );
		}
	}

	@Override
	public String prompt() {
		return "选择御剑目标（消耗3点真元）";
	}
}
