import networkx as nx
import numpy.testing as npt

from GraphRicciCurvature.OllivierRicci import OllivierRicci


def test_compute_ricci_curvature_edges():
    G = nx.karate_club_graph()
    orc = OllivierRicci(G, method="OTD", alpha=0.5)
    output = orc.compute_ricci_curvature_edges([(0, 1)])

    npt.assert_almost_equal(output[0, 1], 0.111111)


def test_compute_ricci_curvature():
    G = nx.karate_club_graph()
    orc = OllivierRicci(G, method="OTD", alpha=0.5)
    Gout = orc.compute_ricci_curvature()
    rc = list(nx.get_edge_attributes(Gout, "ricciCurvature").values())
    ans = [0.111111, -0.143750, 0.041667, -0.114583, -0.281250, -0.281250, 0.062500, -0.200000, -0.114583, 0.062500,
           -0.000000, 0.062500, 0.062500, -0.031250, 0.062500, -0.427083, 0.044444, 0.166667, 0.194444, 0.244444,
           0.166667, 0.111111, 0.166667, -0.041667, 0.050000, 0.125000, 0.100000, 0.100000, 0.200000, -0.175000,
           0.033333, -0.233333, 0.416667, 0.250000, 0.216667, 0.291667, 0.500000, 0.500000, 0.291667, 0.375000,
           0.375000, 0.375000, -0.025000, 0.011765, -0.044118, -0.288235, 0.125000, 0.088235, 0.125000, 0.088235,
           0.125000, 0.088235, -0.254902, 0.125000, 0.088235, 0.125000, 0.088235, 0.100000, 0.225000, 0.200000,
           -0.066667, -0.076471, 0.500000, 0.125000, 0.083333, 0.166667, 0.375000, -0.073529, -0.147059, 0.166667,
           -0.068627, -0.041667, -0.014706, -0.041667, -0.044118, -0.166667, -0.122549, 0.267157]

    npt.assert_array_almost_equal(rc, ans)


def test_compute_ricci_flow():
    G = nx.karate_club_graph()
    orc = OllivierRicci(G, method="OTD", alpha=0.5)
    Gout = orc.compute_ricci_flow(iterations=3)
    rf = list(nx.get_edge_attributes(Gout, "weight").values())
    ans = [0.584642, 1.222957, 0.828566, 1.893597, 2.179315, 2.179315, 0.814135, 1.647656, 1.893597, 0.906430,
           0.916791, 0.798319, 0.760511, 0.829311, 0.760511, 2.477847, 0.937765, 0.681481, 0.612859, 0.568307,
           0.675702, 0.702774, 0.675702, 1.484889, 0.843498, 0.753397, 1.098413, 0.868616, 0.646627, 2.061065,
           1.425968, 1.924123, 0.292387, 0.487378, 0.446435, 0.509673, 0.101477, 0.108645, 0.509673, 0.246037,
           0.246037, 0.228701, 1.309931, 1.213249, 1.317511, 2.149341, 0.712759, 0.811386, 0.712759, 0.811386,
           0.712759, 0.811386, 2.245314, 0.712759, 0.811386, 0.712759, 0.811386, 0.947310, 0.518039, 0.857636,
           1.525740, 1.429449, 0.180896, 0.692919, 0.724545, 0.639637, 0.281116, 1.427853, 1.622385, 0.807457,
           1.386869, 1.372091, 1.320579, 1.324087, 1.276729, 1.843012, 1.721982, 0.412472]

    npt.assert_array_almost_equal(rf, ans)


def test_ricci_community():
    G = nx.karate_club_graph()
    orc = OllivierRicci(G, exp_power=1, alpha=0.5)
    cc = orc.ricci_community()
    ans = {0: 0, 1: 0, 2: 0, 3: 0, 7: 0, 9: 0, 11: 0, 12: 0, 13: 0, 17: 0, 19: 0, 21: 0, 4: 1, 5: 1, 6: 1, 10: 1,
           16: 1, 32: 2, 33: 2, 8: 2, 14: 2, 15: 2, 18: 2, 20: 2, 22: 2, 30: 2, 23: 3, 24: 3, 25: 3, 26: 3, 27: 3,
           28: 3, 29: 3, 31: 3}

    assert cc == ans
