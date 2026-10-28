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
		"别高估自己的力量，使用你能驾驭的武器和护甲。",
		"地牢里并非所有门都一眼可见。如果你卡住了，搜索暗门。",
		"记住，提升力量并非获得更好装备的唯一途径。你可以" +
			"反其道而行，用升级卷轴降低装备的力量需求。",
		"你可以在地牢更深处的商店花金币。第一家商店在第6层。",
			
		"小心胶泥！",
		
		"像素超市——成功冒险所需的一切！",
		"尽快鉴定你的药水和卷轴。别拖到" +
			"真正需要它们的时候。",
		"饥饿不碍事，但极度饥饿会受伤。",
		"突袭命中几率更高。比如，你可以" +
			"知道敌人接近时，躲在关闭的门后伏击。",
		
		"别让天狗出来！",
		
		"像素超市。花钱，活得更久。",
		"当你同时被多个怪物攻击时，试着退到门后。",
		"如果你着火，漂浮时无法在水里灭火。",
		"同时拥有多个安卡没有意义，复活时你会失去它们。",
		
		"危险！重型机械可能造成伤害、断肢或死亡！",
		
		"像素超市。地牢里更安全的生活。",
		"升级附魔武器时，有可能破坏该附魔。",
		"武器和护甲比法杖、戒指损耗更快，但修复方法也更多。",
		"获得湮灭卷轴的唯一途径，是地牢怨灵的馈赠。",
		
		"国王陛下在场，禁止携带武器！",
		
		"像素超市。恶魔猎手专享价！"
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
