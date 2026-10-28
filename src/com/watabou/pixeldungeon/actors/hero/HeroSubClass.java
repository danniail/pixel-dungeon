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
package com.watabou.pixeldungeon.actors.hero;

import com.watabou.utils.Bundle;

public enum HeroSubClass {

	NONE( null, null ),
	
	GLADIATOR( "gladiator", 
		"用近战武器成功攻击后，_角斗士_ 可以发起连击，" +
		"每一次成功命中都会造成更多伤害。" ),
	BERSERKER( "berserker", 
		"当身负重伤时，_狂战士_ 会进入狂野的暴怒状态，" +
		"显著提升伤害输出。" ),
	
	WARLOCK( "warlock", 
		"杀死敌人后，_术士_ 会吞噬它的灵魂，" +
		"治愈他的伤口并缓解饥饿。" ),
	BATTLEMAGE( "battlemage", 
		"手持法杖战斗时，_战斗法师_ 会根据当前充能数造成额外伤害，" +
		"每次成功命中会为该法杖恢复1点充能。" ),
	
	ASSASSIN( "assassin", 
		"进行突袭时，_刺客_ 会对目标造成额外伤害。" ),
	FREERUNNER( "freerunner", 
		"_疾行者_ 的移动速度几乎是大多数怪物的两倍。奔跑时，" +
		"疾行者更难被击中。为此他必须身无负重、且不处于饥饿状态。" ),
		
	SNIPER( "sniper", 
		"_狙击手_ 能发现敌人护甲的弱点，" +
		"使用远程武器时能有效无视护甲。" ),
	WARDEN( "warden", 
		"与自然之力的强烈联系，让 _守望者_ 能从植物中收集露珠和种子。" +
		"此外，踩踏高草会给予他们临时的护甲增益。" );
	
	private String title;
	private String desc;
	
	private HeroSubClass( String title, String desc ) {
		this.title = title;
		this.desc = desc;
	}
	
	public String title() {
		return title;
	}
	
	public String desc() {
		return desc;
	}
	
	private static final String SUBCLASS	= "subClass";
	
	public void storeInBundle( Bundle bundle ) {
		bundle.put( SUBCLASS, toString() );
	}
	
	public static HeroSubClass restoreInBundle( Bundle bundle ) {
		String value = bundle.getString( SUBCLASS );
		try {
			return valueOf( value );
		} catch (Exception e) {
			return NONE;
		}
	}
	
}
