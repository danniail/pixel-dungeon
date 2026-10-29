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
package com.watabou.pixeldungeon;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;

import com.watabou.noosa.Game;
import com.watabou.pixeldungeon.actors.mobs.Acidic;
import com.watabou.pixeldungeon.actors.mobs.Albino;
import com.watabou.pixeldungeon.actors.mobs.Bandit;
import com.watabou.pixeldungeon.actors.mobs.Mob;
import com.watabou.pixeldungeon.actors.mobs.Senior;
import com.watabou.pixeldungeon.actors.mobs.Shielded;
import com.watabou.pixeldungeon.items.Item;
import com.watabou.pixeldungeon.items.bags.ScrollHolder;
import com.watabou.pixeldungeon.items.bags.SeedPouch;
import com.watabou.pixeldungeon.items.bags.WandHolster;
import com.watabou.pixeldungeon.items.potions.Potion;
import com.watabou.pixeldungeon.items.rings.Ring;
import com.watabou.pixeldungeon.items.rings.RingOfHaggler;
import com.watabou.pixeldungeon.items.rings.RingOfThorns;
import com.watabou.pixeldungeon.items.scrolls.Scroll;
import com.watabou.pixeldungeon.items.wands.Wand;
import com.watabou.pixeldungeon.scenes.PixelScene;
import com.watabou.pixeldungeon.utils.GLog;
import com.watabou.utils.Bundle;
import com.watabou.utils.Callback;

public class Badges {
	
	public static enum Badge {
		MONSTERS_SLAIN_1( "击杀10个敌人", 0 ),
		MONSTERS_SLAIN_2( "击杀50个敌人", 1 ),
		MONSTERS_SLAIN_3( "击杀150个敌人", 2 ),
		MONSTERS_SLAIN_4( "击杀250个敌人", 3 ),
		GOLD_COLLECTED_1( "收集100灵石", 4 ),
		GOLD_COLLECTED_2( "收集500灵石", 5 ),
		GOLD_COLLECTED_3( "收集2500灵石", 6 ),
		GOLD_COLLECTED_4( "收集7500灵石", 7 ),
		LEVEL_REACHED_1( "达到6级", 8 ),
		LEVEL_REACHED_2( "达到12级", 9 ),
		LEVEL_REACHED_3( "达到18级", 10 ),
		LEVEL_REACHED_4( "达到24级", 11 ),
		ALL_POTIONS_IDENTIFIED( "鉴定全部丹药", 16 ),
		ALL_SCROLLS_IDENTIFIED( "鉴定全部符箓", 17 ),
		ALL_RINGS_IDENTIFIED( "鉴定全部法宝", 18 ),
		ALL_WANDS_IDENTIFIED( "鉴定全部法器", 19 ),
		ALL_ITEMS_IDENTIFIED( "鉴定全部丹药、符箓、法宝和法器", 35, true ),
		BAG_BOUGHT_SEED_POUCH,
		BAG_BOUGHT_SCROLL_HOLDER,
		BAG_BOUGHT_WAND_HOLSTER,
		ALL_BAGS_BOUGHT( "买下全部储物袋", 23 ),
		DEATH_FROM_FIRE( "死于火焰", 24 ),
		DEATH_FROM_POISON( "死于剧毒", 25 ),
		DEATH_FROM_GAS( "死于毒气", 26 ),
		DEATH_FROM_HUNGER( "死于饥饿", 27 ),
		DEATH_FROM_GLYPH( "死于祭炼", 57 ),
		DEATH_FROM_FALLING( "坠落而死", 59 ),
		YASD( "死于火焰、剧毒、毒气和饥饿", 34, true ),
		BOSS_SLAIN_1_WARRIOR,
		BOSS_SLAIN_1_MAGE,
		BOSS_SLAIN_1_ROGUE,
		BOSS_SLAIN_1_HUNTRESS,
		BOSS_SLAIN_1( "击杀第1个BOSS", 12 ),
		BOSS_SLAIN_2( "击杀第2个BOSS", 13 ),
		BOSS_SLAIN_3( "击杀第3个BOSS", 14 ),
		BOSS_SLAIN_4( "击杀第4个BOSS", 15 ),
		BOSS_SLAIN_1_ALL_CLASSES( "体修、修仙者、刺客和御兽各击杀第1个妖王", 32, true ),
		BOSS_SLAIN_3_GLADIATOR,
		BOSS_SLAIN_3_BERSERKER,
		BOSS_SLAIN_3_WARLOCK,
		BOSS_SLAIN_3_BATTLEMAGE,
		BOSS_SLAIN_3_FREERUNNER,
		BOSS_SLAIN_3_ASSASSIN,
		BOSS_SLAIN_3_SNIPER,
		BOSS_SLAIN_3_WARDEN,
		BOSS_SLAIN_3_ALL_SUBCLASSES( 
			"斗修、血修、剑修、魂修、御风、影杀、神射和御灵各击杀第3个妖王", 33, true ),
		RING_OF_HAGGLER( "获得议价之戒", 20 ),
		RING_OF_THORNS( "获得荆棘之戒", 21 ),
		STRENGTH_ATTAINED_1( "力道达到13点", 40 ),
		STRENGTH_ATTAINED_2( "力道达到15点", 41 ),
		STRENGTH_ATTAINED_3( "力道达到17点", 42 ),
		STRENGTH_ATTAINED_4( "力道达到19点", 43 ),
		FOOD_EATEN_1( "进食10次", 44 ),
		FOOD_EATEN_2( "进食20次", 45 ),
		FOOD_EATEN_3( "进食30次", 46 ),
		FOOD_EATEN_4( "进食40次", 47 ),
		MASTERY_WARRIOR,
		MASTERY_MAGE,
		MASTERY_ROGUE,
		MASTERY_HUNTRESS,
		ITEM_LEVEL_1( "获得3级物品", 48 ),
		ITEM_LEVEL_2( "获得6级物品", 49 ),
		ITEM_LEVEL_3( "获得9级物品", 50 ),
		ITEM_LEVEL_4( "获得12级物品", 51 ),
		RARE_ALBINO,
		RARE_BANDIT,
		RARE_SHIELDED,
		RARE_SENIOR,
		RARE_ACIDIC,
		RARE( "击杀全部稀有妖兽", 37, true ),
		VICTORY_WARRIOR,
		VICTORY_MAGE,
		VICTORY_ROGUE,
		VICTORY_HUNTRESS,
		VICTORY( "获得飞升仙宝", 22 ),
		VICTORY_ALL_CLASSES( "体修、修仙者、刺客和御兽各取得仙宝", 36, true ),
		MASTERY_COMBO( "7连击", 56 ),
		POTIONS_COOKED_1( "炼制3瓶丹药", 52 ),
		POTIONS_COOKED_2( "炼制6瓶丹药", 53 ),
		POTIONS_COOKED_3( "炼制9瓶丹药", 54 ),
		POTIONS_COOKED_4( "炼制12瓶丹药", 55 ),
		NO_MONSTERS_SLAIN( "不杀任何妖兽通关", 28 ),
		GRIM_WEAPON( "用死神之镰击杀妖兽", 29 ),
		PIRANHAS( "击杀6条食人鱼", 30 ),
		NIGHT_HUNTER( "夜间击杀15个妖兽", 58 ),
		GAMES_PLAYED_1( "进行10场游戏", 60, true ),
		GAMES_PLAYED_2( "进行100场游戏", 61, true ),
		GAMES_PLAYED_3( "进行500场游戏", 62, true ),
		GAMES_PLAYED_4( "进行2000场游戏", 63, true ),
		HAPPY_END( "圆满结局", 38 ),
		CHAMPION( "挑战胜利", 39, true ),
		SUPPORTER( "感谢你的支持！", 31, true );
		
		public boolean meta;
		
		public String description;
		public int image;
		
		private Badge( String description, int image ) {
			this( description, image, false );
		}
		
		private Badge( String description, int image, boolean meta ) {
			this.description = description;
			this.image = image;
			this.meta = meta;
		}
		
		private Badge() {
			this( "", -1 );
		}
	}
	
	private static HashSet<Badge> global;
	private static HashSet<Badge> local = new HashSet<Badges.Badge>();
	
	private static boolean saveNeeded = false;
	
	public static Callback loadingListener = null;
	
	public static void reset() {
		local.clear();
		loadGlobal();
	}
	
	private static final String BADGES_FILE	= "badges.dat";
	private static final String BADGES		= "badges";
	
	private static HashSet<Badge> restore( Bundle bundle ) {
		HashSet<Badge> badges = new HashSet<Badge>();
		
		String[] names = bundle.getStringArray( BADGES );
		for (int i=0; i < names.length; i++) {
			try {
				badges.add( Badge.valueOf( names[i] ) );
			} catch (Exception e) {
			}
		}
	
		return badges;
	}
	
	private static void store( Bundle bundle, HashSet<Badge> badges ) {
		int count = 0;
		String names[] = new String[badges.size()];
		
		for (Badge badge:badges) {
			names[count++] = badge.toString();
		}
		bundle.put( BADGES, names );
	}
	
	public static void loadLocal( Bundle bundle ) {
		local = restore( bundle );
	}
	
	public static void saveLocal( Bundle bundle ) {
		store( bundle, local );
	}
	
	public static void loadGlobal() {
		if (global == null) {
			try {
				InputStream input = Game.instance.openFileInput( BADGES_FILE );
				Bundle bundle = Bundle.read( input );
				input.close();
				
				global = restore( bundle );
				
			} catch (IOException e) {
				global = new HashSet<Badge>();
			}
		}
	}
	
	public static void saveGlobal() {
		
		Bundle bundle = null;
		
		if (saveNeeded) {
			
			bundle = new Bundle();
			store( bundle, global );
			
			try {
				OutputStream output = Game.instance.openFileOutput( BADGES_FILE, Game.MODE_PRIVATE );
				Bundle.write( bundle, output );
				output.close();
				saveNeeded = false;
			} catch (IOException e) {
				
			}
		}
	}

	public static void validateMonstersSlain() {
		Badge badge = null;
		
		if (!local.contains( Badge.MONSTERS_SLAIN_1 ) && Statistics.enemiesSlain >= 10) {
			badge = Badge.MONSTERS_SLAIN_1;
			local.add( badge );
		}
		if (!local.contains( Badge.MONSTERS_SLAIN_2 ) && Statistics.enemiesSlain >= 50) {
			badge = Badge.MONSTERS_SLAIN_2;
			local.add( badge );
		}
		if (!local.contains( Badge.MONSTERS_SLAIN_3 ) && Statistics.enemiesSlain >= 150) {
			badge = Badge.MONSTERS_SLAIN_3;
			local.add( badge );
		}
		if (!local.contains( Badge.MONSTERS_SLAIN_4 ) && Statistics.enemiesSlain >= 250) {
			badge = Badge.MONSTERS_SLAIN_4;
			local.add( badge );
		}
		
		displayBadge( badge );
	}
	
	public static void validateGoldCollected() {
		Badge badge = null;
		
		if (!local.contains( Badge.GOLD_COLLECTED_1 ) && Statistics.goldCollected >= 100) {
			badge = Badge.GOLD_COLLECTED_1;
			local.add( badge );
		}
		if (!local.contains( Badge.GOLD_COLLECTED_2 ) && Statistics.goldCollected >= 500) {
			badge = Badge.GOLD_COLLECTED_2;
			local.add( badge );
		}
		if (!local.contains( Badge.GOLD_COLLECTED_3 ) && Statistics.goldCollected >= 2500) {
			badge = Badge.GOLD_COLLECTED_3;
			local.add( badge );
		}
		if (!local.contains( Badge.GOLD_COLLECTED_4 ) && Statistics.goldCollected >= 7500) {
			badge = Badge.GOLD_COLLECTED_4;
			local.add( badge );
		}
		
		displayBadge( badge );
	}
	
	public static void validateLevelReached() {
		Badge badge = null;
		
		if (!local.contains( Badge.LEVEL_REACHED_1 ) && Dungeon.hero.lvl >= 6) {
			badge = Badge.LEVEL_REACHED_1;
			local.add( badge );
		}
		if (!local.contains( Badge.LEVEL_REACHED_2 ) && Dungeon.hero.lvl >= 12) {
			badge = Badge.LEVEL_REACHED_2;
			local.add( badge );
		}
		if (!local.contains( Badge.LEVEL_REACHED_3 ) && Dungeon.hero.lvl >= 18) {
			badge = Badge.LEVEL_REACHED_3;
			local.add( badge );
		}
		if (!local.contains( Badge.LEVEL_REACHED_4 ) && Dungeon.hero.lvl >= 24) {
			badge = Badge.LEVEL_REACHED_4;
			local.add( badge );
		}
		
		displayBadge( badge );
	}
	
	public static void validateStrengthAttained() {
		Badge badge = null;
		
		if (!local.contains( Badge.STRENGTH_ATTAINED_1 ) && Dungeon.hero.STR >= 13) {
			badge = Badge.STRENGTH_ATTAINED_1;
			local.add( badge );
		}
		if (!local.contains( Badge.STRENGTH_ATTAINED_2 ) && Dungeon.hero.STR >= 15) {
			badge = Badge.STRENGTH_ATTAINED_2;
			local.add( badge );
		}
		if (!local.contains( Badge.STRENGTH_ATTAINED_3 ) && Dungeon.hero.STR >= 17) {
			badge = Badge.STRENGTH_ATTAINED_3;
			local.add( badge );
		}
		if (!local.contains( Badge.STRENGTH_ATTAINED_4 ) && Dungeon.hero.STR >= 19) {
			badge = Badge.STRENGTH_ATTAINED_4;
			local.add( badge );
		}
		
		displayBadge( badge );
	}
	
	public static void validateFoodEaten() {
		Badge badge = null;
		
		if (!local.contains( Badge.FOOD_EATEN_1 ) && Statistics.foodEaten >= 10) {
			badge = Badge.FOOD_EATEN_1;
			local.add( badge );
		}
		if (!local.contains( Badge.FOOD_EATEN_2 ) && Statistics.foodEaten >= 20) {
			badge = Badge.FOOD_EATEN_2;
			local.add( badge );
		}
		if (!local.contains( Badge.FOOD_EATEN_3 ) && Statistics.foodEaten >= 30) {
			badge = Badge.FOOD_EATEN_3;
			local.add( badge );
		}
		if (!local.contains( Badge.FOOD_EATEN_4 ) && Statistics.foodEaten >= 40) {
			badge = Badge.FOOD_EATEN_4;
			local.add( badge );
		}
		
		displayBadge( badge );
	}
	
	public static void validatePotionsCooked() {
		Badge badge = null;
		
		if (!local.contains( Badge.POTIONS_COOKED_1 ) && Statistics.potionsCooked >= 3) {
			badge = Badge.POTIONS_COOKED_1;
			local.add( badge );
		}
		if (!local.contains( Badge.POTIONS_COOKED_2 ) && Statistics.potionsCooked >= 6) {
			badge = Badge.POTIONS_COOKED_2;
			local.add( badge );
		}
		if (!local.contains( Badge.POTIONS_COOKED_3 ) && Statistics.potionsCooked >= 9) {
			badge = Badge.POTIONS_COOKED_3;
			local.add( badge );
		}
		if (!local.contains( Badge.POTIONS_COOKED_4 ) && Statistics.potionsCooked >= 12) {
			badge = Badge.POTIONS_COOKED_4;
			local.add( badge );
		}
		
		displayBadge( badge );
	}
	
	public static void validatePiranhasKilled() {
		Badge badge = null;
		
		if (!local.contains( Badge.PIRANHAS ) && Statistics.piranhasKilled >= 6) {
			badge = Badge.PIRANHAS;
			local.add( badge );
		}
		
		displayBadge( badge );
	}
	
	public static void validateItemLevelAquired( Item item ) {
		
		// This method should be called:
		// 1) When an item gets obtained (Item.collect)
		// 2) When an item gets upgraded (ScrollOfUpgrade, ScrollOfWeaponUpgrade, ShortSword, WandOfMagicMissile)
		// 3) When an item gets identified
		if (!item.levelKnown) {
			return;
		}
		
		Badge badge = null;
		
		if (!local.contains( Badge.ITEM_LEVEL_1 ) && item.level() >= 3) {
			badge = Badge.ITEM_LEVEL_1;
			local.add( badge );
		}
		if (!local.contains( Badge.ITEM_LEVEL_2 ) && item.level() >= 6) {
			badge = Badge.ITEM_LEVEL_2;
			local.add( badge );
		}
		if (!local.contains( Badge.ITEM_LEVEL_3 ) && item.level() >= 9) {
			badge = Badge.ITEM_LEVEL_3;
			local.add( badge );
		}
		if (!local.contains( Badge.ITEM_LEVEL_4 ) && item.level() >= 12) {
			badge = Badge.ITEM_LEVEL_4;
			local.add( badge );
		}
		
		displayBadge( badge );
	}
	
	public static void validateAllPotionsIdentified() {
		if (Dungeon.hero != null && Dungeon.hero.isAlive() && 
			!local.contains( Badge.ALL_POTIONS_IDENTIFIED ) && Potion.allKnown()) {
			
			Badge badge = Badge.ALL_POTIONS_IDENTIFIED;
			local.add( badge );
			displayBadge( badge );
			
			validateAllItemsIdentified();
		}
	}
	
	public static void validateAllScrollsIdentified() {
		if (Dungeon.hero != null && Dungeon.hero.isAlive() && 
			!local.contains( Badge.ALL_SCROLLS_IDENTIFIED ) && Scroll.allKnown()) {
			
			Badge badge = Badge.ALL_SCROLLS_IDENTIFIED;
			local.add( badge );
			displayBadge( badge );
			
			validateAllItemsIdentified();
		}
	}
	
	public static void validateAllRingsIdentified() {
		if (Dungeon.hero != null && Dungeon.hero.isAlive() && 
			!local.contains( Badge.ALL_RINGS_IDENTIFIED ) && Ring.allKnown()) {
			
			Badge badge = Badge.ALL_RINGS_IDENTIFIED;
			local.add( badge );
			displayBadge( badge );
			
			validateAllItemsIdentified();
		}
	}
	
	public static void validateAllWandsIdentified() {
		if (Dungeon.hero != null && Dungeon.hero.isAlive() && 
			!local.contains( Badge.ALL_WANDS_IDENTIFIED ) && Wand.allKnown()) {
			
			Badge badge = Badge.ALL_WANDS_IDENTIFIED;
			local.add( badge );
			displayBadge( badge );
			
			validateAllItemsIdentified();
		}
	}
	
	public static void validateAllBagsBought( Item bag ) {
		
		Badge badge = null;
		if (bag instanceof SeedPouch) {
			badge = Badge.BAG_BOUGHT_SEED_POUCH;
		} else if (bag instanceof ScrollHolder) {
			badge = Badge.BAG_BOUGHT_SCROLL_HOLDER;
		} else if (bag instanceof WandHolster) {
			badge = Badge.BAG_BOUGHT_WAND_HOLSTER;
		}
		
		if (badge != null) {
			
			local.add( badge );
			
			if (!local.contains( Badge.ALL_BAGS_BOUGHT ) &&
				local.contains( Badge.BAG_BOUGHT_SCROLL_HOLDER ) &&
				local.contains( Badge.BAG_BOUGHT_SEED_POUCH ) &&
				local.contains( Badge.BAG_BOUGHT_WAND_HOLSTER )) {
						
					badge = Badge.ALL_BAGS_BOUGHT;
					local.add( badge );
					displayBadge( badge );
			}
		}
	}
	
	public static void validateAllItemsIdentified() {
		if (!global.contains( Badge.ALL_ITEMS_IDENTIFIED ) &&
			global.contains( Badge.ALL_POTIONS_IDENTIFIED ) &&
			global.contains( Badge.ALL_SCROLLS_IDENTIFIED ) &&
			global.contains( Badge.ALL_RINGS_IDENTIFIED ) &&
			global.contains( Badge.ALL_WANDS_IDENTIFIED )) {
			
			Badge badge = Badge.ALL_ITEMS_IDENTIFIED;
			displayBadge( badge );
		}
	}
	
	public static void validateDeathFromFire() {
		Badge badge = Badge.DEATH_FROM_FIRE;
		local.add( badge );
		displayBadge( badge );
		
		validateYASD();
	}
	
	public static void validateDeathFromPoison() {
		Badge badge = Badge.DEATH_FROM_POISON;
		local.add( badge );
		displayBadge( badge );
		
		validateYASD();
	}
	
	public static void validateDeathFromGas() {
		Badge badge = Badge.DEATH_FROM_GAS;
		local.add( badge );
		displayBadge( badge );
		
		validateYASD();
	}
	
	public static void validateDeathFromHunger() {
		Badge badge = Badge.DEATH_FROM_HUNGER;
		local.add( badge );
		displayBadge( badge );
		
		validateYASD();
	}
	
	public static void validateDeathFromGlyph() {
		Badge badge = Badge.DEATH_FROM_GLYPH;
		local.add( badge );
		displayBadge( badge );
	}
	
	public static void validateDeathFromFalling() {
		Badge badge = Badge.DEATH_FROM_FALLING;
		local.add( badge );
		displayBadge( badge );
	}
	
	private static void validateYASD() {
		if (global.contains( Badge.DEATH_FROM_FIRE ) &&
			global.contains( Badge.DEATH_FROM_POISON ) &&
			global.contains( Badge.DEATH_FROM_GAS ) &&
			global.contains( Badge.DEATH_FROM_HUNGER)) {
			
			Badge badge = Badge.YASD;
			local.add( badge );
			displayBadge( badge );
		}
	}
	
	public static void validateBossSlain() {
		Badge badge = null;
		switch (Dungeon.depth) {
		case 5:
			badge = Badge.BOSS_SLAIN_1;
			break;
		case 10:
			badge = Badge.BOSS_SLAIN_2;
			break;
		case 15:
			badge = Badge.BOSS_SLAIN_3;
			break;
		case 20:
			badge = Badge.BOSS_SLAIN_4;
			break;
		}
		
		if (badge != null) {
			local.add( badge );
			displayBadge( badge );
			
			if (badge == Badge.BOSS_SLAIN_1) {
				switch (Dungeon.hero.heroClass) {
				case WARRIOR:
					badge = Badge.BOSS_SLAIN_1_WARRIOR;
					break;
				case MAGE:
					badge = Badge.BOSS_SLAIN_1_MAGE;
					break;
				case ROGUE:
					badge = Badge.BOSS_SLAIN_1_ROGUE;
					break;
				case HUNTRESS:
					badge = Badge.BOSS_SLAIN_1_HUNTRESS;
					break;
				}
				local.add( badge );
				if (!global.contains( badge )) {
					global.add( badge );
					saveNeeded = true;
				}
				
				if (global.contains( Badge.BOSS_SLAIN_1_WARRIOR ) &&
					global.contains( Badge.BOSS_SLAIN_1_MAGE ) &&
					global.contains( Badge.BOSS_SLAIN_1_ROGUE ) &&
					global.contains( Badge.BOSS_SLAIN_1_HUNTRESS)) {
					
					badge = Badge.BOSS_SLAIN_1_ALL_CLASSES;
					if (!global.contains( badge )) {
						displayBadge( badge );
						global.add( badge );
						saveNeeded = true;
					}
				}
			} else
			if (badge == Badge.BOSS_SLAIN_3) {
				switch (Dungeon.hero.subClass) {
				case GLADIATOR:
					badge = Badge.BOSS_SLAIN_3_GLADIATOR;
					break;
				case BERSERKER:
					badge = Badge.BOSS_SLAIN_3_BERSERKER;
					break;
				case WARLOCK:
					badge = Badge.BOSS_SLAIN_3_WARLOCK;
					break;
				case BATTLEMAGE:
					badge = Badge.BOSS_SLAIN_3_BATTLEMAGE;
					break;
				case FREERUNNER:
					badge = Badge.BOSS_SLAIN_3_FREERUNNER;
					break;
				case ASSASSIN:
					badge = Badge.BOSS_SLAIN_3_ASSASSIN;
					break;
				case SNIPER:
					badge = Badge.BOSS_SLAIN_3_SNIPER;
					break;
				case WARDEN:
					badge = Badge.BOSS_SLAIN_3_WARDEN;
					break;
				default:
					return;
				}
				local.add( badge );
				if (!global.contains( badge )) {
					global.add( badge );
					saveNeeded = true;
				}
				
				if (global.contains( Badge.BOSS_SLAIN_3_GLADIATOR ) &&
					global.contains( Badge.BOSS_SLAIN_3_BERSERKER ) &&
					global.contains( Badge.BOSS_SLAIN_3_WARLOCK ) &&
					global.contains( Badge.BOSS_SLAIN_3_BATTLEMAGE ) &&
					global.contains( Badge.BOSS_SLAIN_3_FREERUNNER ) &&
					global.contains( Badge.BOSS_SLAIN_3_ASSASSIN ) &&
					global.contains( Badge.BOSS_SLAIN_3_SNIPER ) &&
					global.contains( Badge.BOSS_SLAIN_3_WARDEN )) {
					
					badge = Badge.BOSS_SLAIN_3_ALL_SUBCLASSES;
					if (!global.contains( badge )) {
						displayBadge( badge );
						global.add( badge );
						saveNeeded = true;
					}
				}
			}
		}
	}
	
	public static void validateMastery() {
		
		Badge badge = null;
		switch (Dungeon.hero.heroClass) {
		case WARRIOR:
			badge = Badge.MASTERY_WARRIOR;
			break;
		case MAGE:
			badge = Badge.MASTERY_MAGE;
			break;
		case ROGUE:
			badge = Badge.MASTERY_ROGUE;
			break;
		case HUNTRESS:
			badge = Badge.MASTERY_HUNTRESS;
			break;
		}
		
		if (!global.contains( badge )) {
			global.add( badge );
			saveNeeded = true;
		}
	}
	
	public static void validateMasteryCombo( int n ) {
		if (!local.contains( Badge.MASTERY_COMBO ) && n == 7) {
			Badge badge = Badge.MASTERY_COMBO;
			local.add( badge );
			displayBadge( badge );
		}
	}
	
	public static void validateRingOfHaggler() {
		if (!local.contains( Badge.RING_OF_HAGGLER ) && new RingOfHaggler().isKnown()) {
			Badge badge = Badge.RING_OF_HAGGLER;
			local.add( badge );
			displayBadge( badge );
		}
	}
	
	public static void validateRingOfThorns() {
		if (!local.contains( Badge.RING_OF_THORNS ) && new RingOfThorns().isKnown()) {
			Badge badge = Badge.RING_OF_THORNS;
			local.add( badge );
			displayBadge( badge );
		}
	}
	
	public static void validateRare( Mob mob ) {
		
		Badge badge = null;
		if (mob instanceof Albino) {
			badge = Badge.RARE_ALBINO;
		} else if (mob instanceof Bandit) {
			badge = Badge.RARE_BANDIT;
		} else if (mob instanceof Shielded) {
			badge = Badge.RARE_SHIELDED;
		} else if (mob instanceof Senior) {
			badge = Badge.RARE_SENIOR;
		} else if (mob instanceof Acidic) {
			badge = Badge.RARE_ACIDIC;
		}
		if (!global.contains( badge )) {
			global.add( badge );
			saveNeeded = true;
		}
		
		if (global.contains( Badge.RARE_ALBINO ) &&
			global.contains( Badge.RARE_BANDIT ) &&
			global.contains( Badge.RARE_SHIELDED ) &&
			global.contains( Badge.RARE_SENIOR ) &&
			global.contains( Badge.RARE_ACIDIC )) {
			
			badge = Badge.RARE;
			displayBadge( badge );
		}
	}
	
	public static void validateVictory() {

		Badge badge = Badge.VICTORY;
		displayBadge( badge );

		switch (Dungeon.hero.heroClass) {
		case WARRIOR:
			badge = Badge.VICTORY_WARRIOR;
			break;
		case MAGE:
			badge = Badge.VICTORY_MAGE;
			break;
		case ROGUE:
			badge = Badge.VICTORY_ROGUE;
			break;
		case HUNTRESS:
			badge = Badge.VICTORY_HUNTRESS;
			break;
		}
		local.add( badge );
		if (!global.contains( badge )) {
			global.add( badge );
			saveNeeded = true;
		}
		
		if (global.contains( Badge.VICTORY_WARRIOR ) &&
			global.contains( Badge.VICTORY_MAGE ) &&
			global.contains( Badge.VICTORY_ROGUE ) &&
			global.contains( Badge.VICTORY_HUNTRESS )) {
			
			badge = Badge.VICTORY_ALL_CLASSES;
			displayBadge( badge );
		}
	}
	
	public static void validateNoKilling() {
		if (!local.contains( Badge.NO_MONSTERS_SLAIN ) && Statistics.completedWithNoKilling) {
			Badge badge = Badge.NO_MONSTERS_SLAIN;
			local.add( badge );
			displayBadge( badge );
		}
	}
	
	public static void validateGrimWeapon() {
		if (!local.contains( Badge.GRIM_WEAPON )) {
			Badge badge = Badge.GRIM_WEAPON;
			local.add( badge );
			displayBadge( badge );
		}
	}
	
	public static void validateNightHunter() {
		if (!local.contains( Badge.NIGHT_HUNTER ) && Statistics.nightHunt >= 15) {
			Badge badge = Badge.NIGHT_HUNTER;
			local.add( badge );
			displayBadge( badge );
		}
	}
	
	public static void validateSupporter() {

		global.add( Badge.SUPPORTER );
		saveNeeded = true;
		
		PixelScene.showBadge( Badge.SUPPORTER );
	}
	
	public static void validateGamesPlayed() {
		Badge badge = null;
		if (Rankings.INSTANCE.totalNumber >= 10) {
			badge = Badge.GAMES_PLAYED_1;
		}
		if (Rankings.INSTANCE.totalNumber >= 100) {
			badge = Badge.GAMES_PLAYED_2;
		}
		if (Rankings.INSTANCE.totalNumber >= 500) {
			badge = Badge.GAMES_PLAYED_3;
		}
		if (Rankings.INSTANCE.totalNumber >= 2000) {
			badge = Badge.GAMES_PLAYED_4;
		}
		
		displayBadge( badge );
	}
	
	public static void validateHappyEnd() {
		displayBadge( Badge.HAPPY_END );
	}
	
	public static void validateChampion() {
		displayBadge( Badge.CHAMPION );
	}
	
	private static void displayBadge( Badge badge ) {
		
		if (badge == null) {
			return;
		}
		
		if (global.contains( badge )) {
			
			if (!badge.meta) {
				GLog.h( "徽章已获得：%s", badge.description );
			}
			
		} else {
			
			global.add( badge );
			saveNeeded = true;
			
			if (badge.meta) {
				GLog.h( "新超级徽章：%s", badge.description );
			} else {
				GLog.h( "新徽章：%s", badge.description );
			}	
			PixelScene.showBadge( badge );
		}
	}
	
	public static boolean isUnlocked( Badge badge ) {
		return global.contains( badge );
	}
	
	public static void disown( Badge badge ) {
		loadGlobal();
		global.remove( badge );
		saveNeeded = true;
	}
	
	public static List<Badge> filtered( boolean global ) {
		
		HashSet<Badge> filtered = new HashSet<Badge>( global ? Badges.global : Badges.local );
		
		{
			Iterator<Badge> iterator = filtered.iterator();
			while (iterator.hasNext()) {
				Badge badge = iterator.next();
				if ((!global && badge.meta) || badge.image == -1) {
					iterator.remove();
				}
			}
		}
		
		leaveBest( filtered, Badge.MONSTERS_SLAIN_1, Badge.MONSTERS_SLAIN_2, Badge.MONSTERS_SLAIN_3, Badge.MONSTERS_SLAIN_4 );
		leaveBest( filtered, Badge.GOLD_COLLECTED_1, Badge.GOLD_COLLECTED_2, Badge.GOLD_COLLECTED_3, Badge.GOLD_COLLECTED_4 );
		leaveBest( filtered, Badge.BOSS_SLAIN_1, Badge.BOSS_SLAIN_2, Badge.BOSS_SLAIN_3, Badge.BOSS_SLAIN_4 );
		leaveBest( filtered, Badge.LEVEL_REACHED_1, Badge.LEVEL_REACHED_2, Badge.LEVEL_REACHED_3, Badge.LEVEL_REACHED_4 );
		leaveBest( filtered, Badge.STRENGTH_ATTAINED_1, Badge.STRENGTH_ATTAINED_2, Badge.STRENGTH_ATTAINED_3, Badge.STRENGTH_ATTAINED_4 );
		leaveBest( filtered, Badge.FOOD_EATEN_1, Badge.FOOD_EATEN_2, Badge.FOOD_EATEN_3, Badge.FOOD_EATEN_4 );
		leaveBest( filtered, Badge.ITEM_LEVEL_1, Badge.ITEM_LEVEL_2, Badge.ITEM_LEVEL_3, Badge.ITEM_LEVEL_4 );
		leaveBest( filtered, Badge.POTIONS_COOKED_1, Badge.POTIONS_COOKED_2, Badge.POTIONS_COOKED_3, Badge.POTIONS_COOKED_4 );
		leaveBest( filtered, Badge.BOSS_SLAIN_1_ALL_CLASSES, Badge.BOSS_SLAIN_3_ALL_SUBCLASSES );
		leaveBest( filtered, Badge.DEATH_FROM_FIRE, Badge.YASD );
		leaveBest( filtered, Badge.DEATH_FROM_GAS, Badge.YASD );
		leaveBest( filtered, Badge.DEATH_FROM_HUNGER, Badge.YASD );
		leaveBest( filtered, Badge.DEATH_FROM_POISON, Badge.YASD );
		leaveBest( filtered, Badge.ALL_POTIONS_IDENTIFIED, Badge.ALL_ITEMS_IDENTIFIED );
		leaveBest( filtered, Badge.ALL_SCROLLS_IDENTIFIED, Badge.ALL_ITEMS_IDENTIFIED );
		leaveBest( filtered, Badge.ALL_RINGS_IDENTIFIED, Badge.ALL_ITEMS_IDENTIFIED );
		leaveBest( filtered, Badge.ALL_WANDS_IDENTIFIED, Badge.ALL_ITEMS_IDENTIFIED );
		leaveBest( filtered, Badge.VICTORY, Badge.VICTORY_ALL_CLASSES );
		leaveBest( filtered, Badge.VICTORY, Badge.HAPPY_END );
 		leaveBest( filtered, Badge.VICTORY, Badge.CHAMPION );
		leaveBest( filtered, Badge.GAMES_PLAYED_1, Badge.GAMES_PLAYED_2, Badge.GAMES_PLAYED_3, Badge.GAMES_PLAYED_4 );
		
		ArrayList<Badge> list = new ArrayList<Badge>( filtered );
		Collections.sort( list );
		
		return list;
	}
	
	private static void leaveBest( HashSet<Badge> list, Badge...badges ) {
		for (int i=badges.length-1; i > 0; i--) {
			if (list.contains( badges[i])) {
				for (int j=0; j < i; j++) {
					list.remove( badges[j] );
				}
				break;
			}
		}
	}
}
