def forward_warp(img, flow):
    return softsplat.softsplat(tenIn=img, tenFlow=flow, tenMetric=None, strMode="avg")