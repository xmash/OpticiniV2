/**
 * Theme-agnostic colors for charts and graphs.
 * Use these instead of var(--color-primary) / var(--color-accent-*) so chart
 * colors stay consistent across Professional Slate, Professional Purple, etc.
 */

/** Sequential palette for series (bars, lines, pie segments). Same look in any theme. */
export const CHART_COLORS = [
  "#2563eb", // blue
  "#0d9488", // teal
  "#d97706", // amber
  "#dc2626", // red
  "#7c3aed", // violet
] as const;

export const CHART_COLOR_1 = CHART_COLORS[0];
export const CHART_COLOR_2 = CHART_COLORS[1];
export const CHART_COLOR_3 = CHART_COLORS[2];
export const CHART_COLOR_4 = CHART_COLORS[3];
export const CHART_COLOR_5 = CHART_COLORS[4];

/** Semantic colors for health/status charts (fixed hex, not theme vars). */
export const CHART_SEMANTIC = {
  success: "#16a34a",
  warning: "#ca8a04",
  destructive: "#dc2626",
  info: "#2563eb",
} as const;

/** Grid and axis strokes — neutral, visible on light card background. */
export const CHART_GRID_STROKE = "#e2e8f0";
export const CHART_AXIS_STROKE = "#64748b";

/** Get color by index (wraps around palette). */
export function getChartColor(index: number): string {
  return CHART_COLORS[index % CHART_COLORS.length];
}
