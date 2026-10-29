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
	
	GLADIATOR( "斗修",
		"用近战兵器成功命中后，_斗修_ 可顺势发起连击，" +
		"每一次命中都比上一次更重。" ),
	BERSERKER( "血修",
		"当身负重伤、气血将尽时，_血修_ 会陷入狂暴，" +
		"周身气血翻涌，出手威力大增。" ),
	
	WARLOCK( "魂修", 
		"斩杀敌人后，_魂修_ 会吞噬其魂魄，" +
		"用来疗伤并缓解饥饿。" ),
	BATTLEMAGE( "剑修", 
		"手持法器近身搏杀时，_剑修_ 法器中灵力越足，出手越重，" +
		"每次命中还能为该法器恢复1点灵力。" ),
	
	ASSASSIN( "影杀",
		"潜行突袭时，_影杀_ 会对目标造成额外的致命伤害。" ),
	FREERUNNER( "御风",
		"_御风_ 身法极快，速度几乎是寻常妖兽的两倍；施展身法时，" +
		"更难被击中。但须身无负重、且不在饥饿之中。" ),

	SNIPER( "神射",
		"_神射_ 目光如炬，能洞察敌身破绽，" +
		"御使法器远程攻敌时可无视其护甲。" ),
	WARDEN( "御灵",
		"_御灵_ 与草木灵兽天然亲和，能从灵草中收集晨露与灵种；" +
		"穿行于高草之间时，还会获得短暂的护体灵光。" );
	
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
