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
package com.watabou.pixeldungeon.levels.features;

import com.watabou.noosa.audio.Sample;
import com.watabou.pixeldungeon.Assets;
import com.watabou.pixeldungeon.Dungeon;
import com.watabou.pixeldungeon.effects.CellEmitter;
import com.watabou.pixeldungeon.effects.particles.ElmoParticle;
import com.watabou.pixeldungeon.levels.DeadEndLevel;
import com.watabou.pixeldungeon.levels.Terrain;
import com.watabou.pixeldungeon.scenes.GameScene;
import com.watabou.pixeldungeon.utils.GLog;
import com.watabou.pixeldungeon.windows.WndMessage;

public class Sign {

	private static final String TXT_DEAD_END = 
		"你在这里做什么？！";
	
	private static final String[] TIPS = {
		"别高估自己的力道，使用你能驾驭的兵器和护甲。",
		"秘境里并非所有门都一眼可见。如果你卡住了，搜索暗门。",
		"记住，提升力道并非获得更好装备的唯一途径。你可以" +
			"反其道而行，用强化符降低装备的力道需求。",
		"你可以在秘境更深处的坊市花灵石。第一家坊市在第6层。",
			
		"小心胶泥！",
		
		"修仙坊市——成功冒险所需的一切！",
		"尽快鉴定你的丹药和符箓。别拖到" +
			"真正需要它们的时候。",
		"饥饿不碍事，但极度饥饿会受伤。",
		"突袭命中几率更高。比如，你可以" +
			"知道敌人接近时，躲在关闭的门后伏击。",
		
		"别让天狗出来！",
		
		"修仙坊市。花灵石，活得更久。",
		"当你同时被多个妖兽攻击时，试着退到门后。",
		"如果你着火，漂浮时无法在水里灭火。",
		"同时拥有多枚转生玉没有意义，复生时你会失去它们。",
		
		"危险！重型傀儡可能造成伤害、断肢或死亡！",
		
		"修仙坊市。秘境里更安全的修行。",
		"强化祭炼过的兵器时，有可能破坏其上的祭炼。",
		"兵器和护甲比法器、法宝损耗更快，但修复方法也更多。",
		"获得灭灵符的唯一途径，是秘境怨灵的馈赠。",
		
		"傀儡之主在场，禁止携带兵器！",
		
		"修仙坊市。修仙者专享价！"
	};
	
	private static final String TXT_BURN =
		"你试图读告示牌时，它爆成绿色的火焰。";
	
	public static void read( int pos ) {
		
		if (Dungeon.level instanceof DeadEndLevel) {
			
			GameScene.show( new WndMessage( TXT_DEAD_END ) );
			
		} else {
			
			int index = Dungeon.depth - 1;
			
			if (index < TIPS.length) {
				GameScene.show( new WndMessage( TIPS[index] ) );
			} else {
				
				Dungeon.level.destroy( pos );
				GameScene.updateMap( pos );
				GameScene.discoverTile( pos, Terrain.SIGN );
				
				CellEmitter.get( pos ).burst( ElmoParticle.FACTORY, 6 );
				Sample.INSTANCE.play( Assets.SND_BURNING );
				
				GLog.w( TXT_BURN );
				
			}
		}
	}
}
