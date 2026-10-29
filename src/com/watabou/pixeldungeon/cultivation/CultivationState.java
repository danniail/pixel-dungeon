/*
 * Persistent cultivation state, independent from the original hero save fields.
 */
package com.watabou.pixeldungeon.cultivation;

import com.watabou.utils.Bundle;

public class CultivationState implements com.watabou.utils.Bundlable {

	private static final String TRUE_ESSENCE	= "trueEssence";
	private static final String RECOVERY_TURNS	= "recoveryTurns";
	private static final String FOUNDATION		= "foundationDone";
	private static final String TECHNIQUE		= "qingyunKnown";
	private static final String PENDING			= "breakthroughPending";

	public int trueEssence = 0;
	public int recoveryTurns = 0;
	public boolean foundationDone = false;
	public boolean qingyunKnown = false;
	public boolean breakthroughPending = false;

	public int maxTrueEssence() {
		return foundationDone ? 10 : 0;
	}

	public void storeInBundle( Bundle bundle ) {
		bundle.put( TRUE_ESSENCE, trueEssence );
		bundle.put( RECOVERY_TURNS, recoveryTurns );
		bundle.put( FOUNDATION, foundationDone );
		bundle.put( TECHNIQUE, qingyunKnown );
		bundle.put( PENDING, breakthroughPending );
	}

	public void restoreFromBundle( Bundle bundle ) {
		trueEssence = bundle.getInt( TRUE_ESSENCE );
		recoveryTurns = bundle.getInt( RECOVERY_TURNS );
		foundationDone = bundle.getBoolean( FOUNDATION );
		qingyunKnown = bundle.getBoolean( TECHNIQUE );
		breakthroughPending = bundle.getBoolean( PENDING );

		// Migration for M1 saves and defensive recovery from interrupted writes.
		if (!foundationDone) {
			trueEssence = 0;
			recoveryTurns = 0;
			qingyunKnown = false;
		} else {
			trueEssence = Math.max( 0, Math.min( trueEssence, maxTrueEssence() ) );
		}
	}
}
