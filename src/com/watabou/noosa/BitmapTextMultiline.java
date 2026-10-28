/*
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

package com.watabou.noosa;

import java.util.ArrayList;
import java.util.LinkedHashMap;

import android.graphics.RectF;

import com.watabou.glwrap.Quad;
import com.watabou.utils.PointF;

public class BitmapTextMultiline extends BitmapText {

	public int maxWidth = Integer.MAX_VALUE;

	public int nLines = 0;

	public boolean[] mask;

	public BitmapTextMultiline( Font font ) {
		this( "", font );
	}

	public BitmapTextMultiline( String text, Font font ) {
		super( text, font );
	}

	// A character that can break a line on its own (CJK ideographs,
	// CJK punctuation and fullwidth forms).
	protected static boolean isCjk( char c ) {
		return (c >= 0x4E00 && c <= 0x9FFF)
			|| (c >= 0x3400 && c <= 0x4DBF)
			|| (c >= 0x3000 && c <= 0x303F)
			|| (c >= 0xFF00 && c <= 0xFFEF);
	}

	// One positioned character produced by the layout pass.
	protected static class Placed {
		char ch;
		float x, y, w, h;
		Placed( char ch, float x, float y, float w, float h ) {
			this.ch = ch; this.x = x; this.y = y; this.w = w; this.h = h;
		}
	}

	protected static class Layout {
		ArrayList<Placed> chars = new ArrayList<Placed>();
		float width = 0;
		float height = 0;
		int lines = 0;
	}

	/**
	 * Mixed Chinese/English layout. Latin runs are kept whole and separated
	 * by spaces, while each CJK character is an independent break point.
	 */
	protected Layout doLayout() {
		Layout layout = new Layout();
		if (text == null) {
			text = "";
		}

		float spaceSize = font.width( font.get( ' ' ) );
		float limit = maxWidth / scale.x;

		float lineX = 0;       // width consumed on the current line
		float lineH = 0;       // tallest run on the current line
		float y = 0;
		int lines = 1;
		boolean content = false; // anything placed on the current line
		boolean wantSpace = false; // a space requested before the next Latin run

		int len = text.length();
		int i = 0;
		while (i < len) {
			char c = text.charAt( i );

			if (c == '\n') {
				// Hard line break.
				layout.width = Math.max( layout.width, lineX );
				layout.height += lineH;
				lines++;
				lineX = 0; lineH = 0; y = layout.height;
				content = false; wantSpace = false;
				i++;
				continue;
			}

			if (c == ' ') {
				if (content) {
					wantSpace = true;
				}
				i++;
				continue;
			}

			// Find the extent of this run: a single CJK character, or a
			// maximal run of non-space, non-CJK Latin characters.
			int end;
			if (isCjk( c )) {
				end = i + 1;
			} else {
				end = i;
				while (end < len
					&& text.charAt( end ) != ' '
					&& text.charAt( end ) != '\n'
					&& !isCjk( text.charAt( end ) )) {
					end++;
				}
			}

			// Measure the run.
			float runW = 0, runH = 0;
			for (int k = i; k < end; k++) {
				RectF r = font.get( text.charAt( k ) );
				runW += font.width( r ) + (k > i ? font.tracking : 0);
				runH = Math.max( runH, font.height( r ) );
			}

			// A space is only inserted between Latin content; it is never
			// inserted before a CJK character.
			boolean addSpace = wantSpace && !isCjk( c );
			float spaceW = addSpace ? spaceSize : 0;

			// Wrap if the run (plus optional space) does not fit.
			if (content && lineX + spaceW + runW > limit) {
				layout.width = Math.max( layout.width, lineX );
				layout.height += lineH;
				lines++;
				lineX = 0; lineH = 0; y = layout.height;
				content = false;
				spaceW = 0;
			}

			if (addSpace) {
				lineX += spaceSize;
			}
			wantSpace = false;

			// Place each character of the run.
			float cx = lineX;
			for (int k = i; k < end; k++) {
				char ch = text.charAt( k );
				RectF r = font.get( ch );
				float cw = font.width( r );
				float chh = font.height( r );
				layout.chars.add( new Placed( ch, cx, y, cw, chh ) );
				cx += cw + font.tracking;
			}
			lineX += runW;
			lineH = Math.max( lineH, runH );
			content = true;

			i = end;
		}

		layout.width = Math.max( layout.width, lineX );
		layout.height += lineH;
		layout.lines = lines;
		return layout;
	}

	@Override
	protected void updateVertices() {
		Layout layout = doLayout();

		quads = Quad.createSet( layout.chars.size() );
		realLength = 0;

		float[] vertices = new float[16];
		int pos = 0;
		for (Placed p : layout.chars) {
			RectF rect = font.get( p.ch );

			if (mask == null || mask[pos]) {
				vertices[0] = p.x;
				vertices[1] = p.y;
				vertices[2] = rect.left;
				vertices[3] = rect.top;

				vertices[4] = p.x + p.w;
				vertices[5] = p.y;
				vertices[6] = rect.right;
				vertices[7] = rect.top;

				vertices[8] = p.x + p.w;
				vertices[9] = p.y + p.h;
				vertices[10] = rect.right;
				vertices[11] = rect.bottom;

				vertices[12] = p.x;
				vertices[13] = p.y + p.h;
				vertices[14] = rect.left;
				vertices[15] = rect.bottom;

				quads.put( vertices );
				realLength++;
			}
			pos++;
		}

		width = layout.width;
		height = layout.height;
		nLines = layout.lines;
		dirty = false;
	}

	@Override
	public void measure() {
		Layout layout = doLayout();
		width = layout.width;
		height = layout.height;
		nLines = layout.lines;
	}

	@Override
	public float baseLine() {
		return (height - font.lineHeight + font.baseLine) * scale.y;
	}

	/**
	 * Splits the laid-out text into one independent BitmapText per physical
	 * line, so callers can position or colour each line separately.
	 */
	public class LineSplitter {

		public ArrayList<BitmapText> split() {
			Layout layout = BitmapTextMultiline.this.doLayout();

			LinkedHashMap<Float, ArrayList<Placed>> byY = new LinkedHashMap<>();
			for (Placed p : layout.chars) {
				byY.computeIfAbsent( p.y, k -> new ArrayList<>() ).add( p );
			}

			float spaceW = font.width( font.get( ' ' ) );
			ArrayList<BitmapText> result = new ArrayList<>();
			for (ArrayList<Placed> line : byY.values()) {
				StringBuilder sb = new StringBuilder();
				float prevRight = -1;
				for (Placed p : line) {
					if (prevRight >= 0 && p.x - prevRight > spaceW * 0.5f) {
						sb.append( ' ' );
					}
					sb.append( p.ch );
					prevRight = p.x + p.w;
				}
				BitmapText t = new BitmapText( sb.toString(), font );
				t.scale.set( scale.x, scale.y );
				result.add( t );
			}
			return result;
		}
	}
}
