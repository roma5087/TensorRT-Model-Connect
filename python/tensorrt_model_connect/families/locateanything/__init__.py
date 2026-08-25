# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""LocateAnything family plugin."""

from .task_contract import (
    Localization,
    detect_text_prompt,
    detection_prompt,
    ground_gui_prompt,
    ground_multi_prompt,
    ground_single_prompt,
    ground_text_prompt,
    matched_box_iou,
    matched_point_distance,
    parse_localizations,
    point_prompt,
)


def __getattr__(name):
    if name == "plugin":
        from .plugin import plugin as _plugin

        return _plugin
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "Localization",
    "detect_text_prompt",
    "detection_prompt",
    "ground_gui_prompt",
    "ground_multi_prompt",
    "ground_single_prompt",
    "ground_text_prompt",
    "matched_box_iou",
    "matched_point_distance",
    "parse_localizations",
    "plugin",
    "point_prompt",
]
