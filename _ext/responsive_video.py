from __future__ import annotations
import html as html_lib
from docutils import nodes
from docutils.parsers.rst import Directive, directives


def _parse_ratio(ratio_str: str) -> tuple[int, int]:
    # Accept "16:9" or "4:3"
    parts = ratio_str.strip().split(":")
    if len(parts) != 2:
        raise ValueError("ratio must be like '16:9'")
    w = int(parts[0])
    h = int(parts[1])
    if w <= 0 or h <= 0:
        raise ValueError("ratio values must be positive")
    return w, h


class VideoDirective(Directive):
    """
    Usage (MyST):

    ```{video} kKKM8Y-u7ds
    :caption: Optional caption text.
    :ratio: 16:9
    :max-width: 900px
    :start: 30
    ```
    """

    required_arguments = 1  # YouTube video id
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = False

    option_spec = {
        "caption": directives.unchanged,
        "ratio": directives.unchanged,        # e.g. "16:9"
        "max-width": directives.unchanged,    # e.g. "560px" or "900px"
        "start": directives.nonnegative_int,  # seconds
        "align": directives.unchanged,   # Added to fix warning
        "height": directives.unchanged,
    }

    def run(self):
        vid = self.arguments[0].strip()

        caption = self.options.get("caption", "").strip()
        ratio = self.options.get("ratio", "16:9").strip()
        max_width = self.options.get("max-width", "").strip()
        start = self.options.get("start", None)
        align = self.options.get("align", "center").strip() # Default to center

        w, h = _parse_ratio(ratio)
        
        # Build YouTube embed URL
        src = f"https://www.youtube.com/embed/{vid}"
        if start is not None and start > 0:
            src += f"?start={start}"

        # Build wrapper styles
        style_bits = [f"aspect-ratio:{w}/{h};"]
        if max_width:
            style_bits.append(f"max-width:{max_width};")
            style_bits.append("margin-left:auto;margin-right:auto;")
        # Handle Alignment
        if align == "left":
            style_bits.append("margin-right: auto; margin-left: 0;")
        elif align == "right":
            style_bits.append("margin-left: auto; margin-right: 0;")
        else:
            # Default center
            style_bits.append("margin-left: auto; margin-right: auto;")
        style_attr = " ".join(style_bits)

        html = [
            f'<div class="video-container" style="{style_attr}">',
            f'  <iframe src="{src}" allowfullscreen '
            f'loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>',
            "</div>",
        ]
        if caption:
            # Use standard HTML escaping instead of nodes.escape2null
            safe_caption = html_lib.escape(caption)
            html.append(f'<div class="video-caption">{safe_caption}</div>')

        raw = nodes.raw("", "\n".join(html), format="html")
        return [raw]


def setup(app):
    app.add_directive("etamu-video", VideoDirective)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
