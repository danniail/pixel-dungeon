/*
 * Cultivation realm mapping. Internal hero.lvl remains the source of truth.
 */
package com.watabou.pixeldungeon.cultivation;

public enum Realm {
	QI( 1, "炼气" ),
	FOUNDATION( 10, "筑基" ),
	CORE( 15, "结丹" ),
	NASCENT( 20, "元婴" ),
	SPIRIT( 25, "化神" );

	public final int level;
	public final String title;

	Realm( int level, String title ) {
		this.level = level;
		this.title = title;
	}

	public static String title( int level ) {
		String title = QI.title;
		for (Realm realm : values()) {
			if (level >= realm.level) {
				title = realm.title;
			}
		}
		return title;
	}
}
