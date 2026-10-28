/*
 * Simplified Chinese font support for Pixel Dungeon.
 * Renders an arbitrary character set (Latin + CJK) into a square-grid
 * bitmap atlas at runtime using the platform Paint, then registers each
 * character as a frame in a BitmapText.Font.
 */
package com.watabou.noosa;

import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.RectF;
import android.graphics.Typeface;

import com.watabou.gltextures.SmartTexture;
import com.watabou.gltextures.TextureCache;

public class CNFont {

	// Every Android device supported by minSdk 21 provides >= 2048 textures.
	private static final int MAX_TEX = 2048;

	/**
	 * @param cell   size of the square cell for one character, in pixels
	 * @param chars  all characters that may be displayed
	 * @param bold   use a bold style (better legibility at small sizes)
	 */
	public static BitmapText.Font create( int cell, String chars, boolean bold ) {

		// De-duplicate characters while preserving order.
		StringBuilder uniq = new StringBuilder();
		boolean[] seen = new boolean[65536];
		for (int i = 0; i < chars.length(); i++) {
			char c = chars.charAt( i );
			if (c == '\r' || c == '\n' || c == '\t') {
				continue;
			}
			if (!seen[c]) {
				seen[c] = true;
				uniq.append( c );
			}
		}
		// A space is always required for layout.
		if (!seen[' ']) {
			uniq.insert( 0, ' ' );
		}

		int count = uniq.length();
		int cols = Math.max( 1, MAX_TEX / cell );
		int rows = (count + cols - 1) / cols;
		int w = cols * cell;
		int h = rows * cell;

		Bitmap bmp = Bitmap.createBitmap( w, h, Bitmap.Config.ARGB_8888 );
		Canvas canvas = new Canvas( bmp );

		Paint paint = new Paint( Paint.ANTI_ALIAS_FLAG );
		paint.setAntiAlias( false );
		paint.setSubpixelText( false );
		paint.setLinearText( false );
		paint.setTypeface( Typeface.create(
			Typeface.DEFAULT, bold ? Typeface.BOLD : Typeface.NORMAL ) );
		paint.setColor( 0xFFFFFFFF );
		// Glyph slightly smaller than the cell so it does not touch the edge.
		paint.setTextSize( cell * 0.92f );
		Paint.FontMetrics fm = paint.getFontMetrics();

		for (int i = 0; i < count; i++) {
			int col = i % cols;
			int row = i / cols;
			float originX = col * cell;
			float centerY = row * cell + cell / 2f;

			String s = String.valueOf( uniq.charAt( i ) );
			float textW = paint.measureText( s );
			float x = originX + (cell - textW) / 2f;
			float baseline = centerY - (fm.ascent + fm.descent) / 2f;
			canvas.drawText( s, x, baseline, paint );
		}

		SmartTexture tx = TextureCache.get( bmp );
		BitmapText.Font font = new BitmapText.Font( tx );

		for (int i = 0; i < count; i++) {
			int col = i % cols;
			int row = i / cols;
			RectF rect = new RectF(
				(float) (col * cell) / w,
				(float) (row * cell) / h,
				(float) ((col + 1) * cell) / w,
				(float) ((row + 1) * cell) / h );
			font.add( uniq.charAt( i ), rect );
		}

		font.lineHeight = cell;
		font.baseLine = cell;
		font.tracking = 0;
		return font;
	}
}
