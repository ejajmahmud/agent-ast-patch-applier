"""AST-validated fuzzy patch applier."""
import ast
from typing import Tuple, Dict, Any


class ASTPatchApplier:
    def apply_patch(self, original_code: str, search_block: str, replace_block: str) -> Tuple[str, Dict[str, Any]]:
        """Replaces search_block with replace_block and verifies AST validity."""
        # Exact match attempt
        if search_block in original_code:
            patched = original_code.replace(search_block, replace_block, 1)
        else:
            # Whitespace normalized fallback
            s_stripped = search_block.strip()
            if s_stripped in original_code:
                patched = original_code.replace(s_stripped, replace_block.strip(), 1)
            else:
                return original_code, {"success": False, "error": "Search block not found"}

        # Validate AST
        try:
            ast.parse(patched)
            return patched, {"success": True, "error": None}
        except SyntaxError as e:
            return original_code, {"success": False, "error": f"AST SyntaxError: {e}"}
