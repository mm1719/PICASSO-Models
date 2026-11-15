# Additional EcoTaxa provenance and evidence

This is a source-evidence ledger, not a grant to redistribute source images and not a representation that data licenses automatically govern learned parameters. Six main datasets are documented in [ATTRIBUTION.md](ATTRIBUTION.md). The following 48 projects comprise A2's additional EcoTaxa data; 47 supply training rows, while 18222 supplies one validation row only.

Counts refer to the preserved A2 split, not current live project sizes. They total 45,734 training, 5,741 validation, and 5,735 test rows. The source split hash is recorded in the model card. No object-level identifiers, images, filesystem paths, or personal contacts are provided.

## Evidence status

- Project **6015** has a precise CC BY 4.0 dataset statement covering imagery. All 3,183 used rows matched the preserved export metadata and published time/location/instrument scope.
- For the **other 47 projects**, a precise image license or agreement covering the used snapshot was not independently established. This does not prove that no such agreement exists or that learned-weight distribution is prohibited.
- Public collection endpoints were checked successfully for all 48 and returned no public collections. Absence of a collection is neither a license nor a prohibition.
- Papers or adjacent published datasets are listed to trace provenance; where they do not cover the exact images, that mismatch is explicit. Chinese notes preserve the wording of the evidence review.

| Project | Source title | Train | Val | Test | Evidence status / qualification | Supporting records |
|---|---|---:|---:|---:|---|---|
| [211](https://ecotaxa.obs-vlfr.fr/prj/211) | Flowcam composite TARA Pacific | 2 | 0 | 0 | TaraPacific公開影像有license但正式project為11341/11353等；須精確子集映射 | [Evidence 1](https://essd.copernicus.org/articles/17/2761/2025/) · [Evidence 2](https://doi.org/10.17882/102697) · [Evidence 3](https://doi.org/10.17882/102694) |
| [253](https://ecotaxa.obs-vlfr.fr/prj/253) | Flowcam point B WP2 50 2016 | 7 | 1 | 0 | PointB精確年份影像條款未確認；2010–2011 PANGAEA生物體積表不能套用 | [Evidence 1](https://doi.pangaea.de/10.1594/PANGAEA.833549) |
| [260](https://ecotaxa.obs-vlfr.fr/prj/260) | Flowcam point B WP2 50 2015 2016 | 58 | 8 | 13 | PointB精確年份影像條款未確認；2010–2011 PANGAEA生物體積表不能套用 | [Evidence 1](https://doi.pangaea.de/10.1594/PANGAEA.833549) |
| [825](https://ecotaxa.obs-vlfr.fr/prj/825) | Flowcam  MooseGE 2017 Triple Net 64 | 681 | 85 | 79 | 正式資料論文Table4精確列FlowCam影像ID；影像本身條款尚未確認 | [Evidence 1](https://essd.copernicus.org/articles/18/5303/2026/essd-18-5303-2026.pdf) |
| [1342](https://ecotaxa.obs-vlfr.fr/prj/1342) | Flowcam Creocean Angola WP2 50 2018 | 4 | 0 | 0 | Creocean精確專案條款未找到；排除南非Block567不同地點年份與僅觀測表 | [Evidence 1](https://ipt.gbif.fr/resource?r=block-567-2022) |
| [1363](https://ecotaxa.obs-vlfr.fr/prj/1363) | Flowcam Lucas TEST | 1 | 0 | 0 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [1534](https://ecotaxa.obs-vlfr.fr/prj/1534) | Flowcam Creocean Mauritanie WP2 50 2018 | 5 | 0 | 0 | Creocean精確專案條款未找到；排除南非Block567不同地點年份與僅觀測表 | [Evidence 1](https://ipt.gbif.fr/resource?r=block-567-2022) |
| [2186](https://ecotaxa.obs-vlfr.fr/prj/2186) | Tara Pacific/deck net : Hawaï > Panama | 8 | 0 | 2 | TaraPacific公開影像有license但正式project為11341/11353等；須精確子集映射 | [Evidence 1](https://essd.copernicus.org/articles/17/2761/2025/) · [Evidence 2](https://doi.org/10.17882/102697) · [Evidence 3](https://doi.org/10.17882/102694) |
| [2278](https://ecotaxa.obs-vlfr.fr/prj/2278) | Flowcam MooseGE 2018 Triple Net 64 | 17 | 3 | 6 | 正式資料論文Table4精確列FlowCam影像ID；影像本身條款尚未確認 | [Evidence 1](https://essd.copernicus.org/articles/18/5303/2026/essd-18-5303-2026.pdf) |
| [2556](https://ecotaxa.obs-vlfr.fr/prj/2556) | Flowcam TAN1901 Bongo Net 64 | 2,185 | 279 | 266 | TAN1901名稱線索但無exactID影像授權；排除未對應的Rhizaria資料包 | [Evidence 1](https://data.mendeley.com/datasets/j9262jxgt8/1) |
| [2557](https://ecotaxa.obs-vlfr.fr/prj/2557) | Flowcam TAN1901 Bottle Net 20 | 12 | 1 | 1 | TAN1901名稱線索但無exactID影像授權；排除未對應的Rhizaria資料包 | [Evidence 1](https://data.mendeley.com/datasets/j9262jxgt8/1) |
| [2740](https://ecotaxa.obs-vlfr.fr/prj/2740) | Flowcam Pollina 2020 20microns | 32 | 4 | 4 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [3097](https://ecotaxa.obs-vlfr.fr/prj/3097) | _Flowcam_Reference | 978 | 122 | 129 | 複合參考庫，WWWPIC資助不是授權；須追實際入訓978列的來源而非一律補全部巢狀projects | Source project metadata; no exact image grant located |
| [3891](https://ecotaxa.obs-vlfr.fr/prj/3891) | Flowcam Tara Microbiomes P2/deck net : Lorient > Punta Arenas | 185 | 32 | 20 | 原論文與官方deliverable精確列ID；文章授權不能直接套外部影像 | [Evidence 1](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2022.916025/full) · [Evidence 2](https://orbi.uliege.be/bitstream/2268/304961/1/AtlantECO_Deliverable_D2.1.pdf) |
| [3892](https://ecotaxa.obs-vlfr.fr/prj/3892) | Flowcam Tara Microbiomes P2/miniHSN: Lorient > Punta Arenas | 420 | 47 | 63 | 原論文與官方deliverable精確列ID；文章授權不能直接套外部影像 | [Evidence 1](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2022.916025/full) · [Evidence 2](https://orbi.uliege.be/bitstream/2268/304961/1/AtlantECO_Deliverable_D2.1.pdf) |
| [3910](https://ecotaxa.obs-vlfr.fr/prj/3910) | Flowcam Creocean Congo WP2 50 2020 | 30 | 6 | 5 | Creocean精確專案條款未找到；排除南非Block567不同地點年份與僅觀測表 | [Evidence 1](https://ipt.gbif.fr/resource?r=block-567-2022) |
| [4063](https://ecotaxa.obs-vlfr.fr/prj/4063) | Flowcam LOG EMAH 2021 | 2 | 0 | 0 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [4424](https://ecotaxa.obs-vlfr.fr/prj/4424) | EcoTeBo_Microzooplankton | 15,130 | 1,911 | 1,903 | 原論文精確連ID；Figshare CC BY只確認12個分析檔，未涵蓋EcoTaxa原圖 | [Evidence 1](https://nsojournals.onlinelibrary.wiley.com/doi/10.1111/oik.10561) · [Evidence 2](https://api.figshare.com/v2/articles/23925291) |
| [6015](https://ecotaxa.obs-vlfr.fr/prj/6015) | FlowCam H2020 EU Mission Atlantic Cabo Frio Upwelling System | 2,542 | 319 | 322 | 官方資料集直接連project且列CC BY4；A2使用3183列全部匹配來源metadata與時空/儀器範圍；不據此變更模型license | [Evidence 1](https://www.vliz.be/en/imis?dasid=8058&module=dataset) |
| [7666](https://ecotaxa.obs-vlfr.fr/prj/7666) | Flowcam point B WP2 50 2023 sn10787 | 383 | 34 | 48 | PointB精確年份影像條款未確認；2010–2011 PANGAEA生物體積表不能套用 | [Evidence 1](https://doi.pangaea.de/10.1594/PANGAEA.833549) |
| [8847](https://ecotaxa.obs-vlfr.fr/prj/8847) | prediction_test | 27 | 4 | 2 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [10750](https://ecotaxa.obs-vlfr.fr/prj/10750) | X3_4x | 5 | 2 | 1 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [11273](https://ecotaxa.obs-vlfr.fr/prj/11273) | ISCO_4x | 1 | 0 | 0 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [11716](https://ecotaxa.obs-vlfr.fr/prj/11716) | Training_Flowprocess_10x_Estuary | 2 | 0 | 0 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [13909](https://ecotaxa.obs-vlfr.fr/prj/13909) | Flowcam Creocean Suriname WP2 50 2024 | 1,246 | 157 | 154 | Creocean精確專案條款未找到；排除南非Block567不同地點年份與僅觀測表 | [Evidence 1](https://ipt.gbif.fr/resource?r=block-567-2022) |
| [13982](https://ecotaxa.obs-vlfr.fr/prj/13982) | GTMNERR SWMP Plankton | 1 | 0 | 0 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [14694](https://ecotaxa.obs-vlfr.fr/prj/14694) | Great Bay Phytoplankton Timeseries 4x | 1 | 0 | 1 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [14791](https://ecotaxa.obs-vlfr.fr/prj/14791) | Lexplore_ALGA_Flowcam_micro | 1,448 | 196 | 169 | 官方ALGA精確連ID；來源身分確認，影像條款未確認 | [Evidence 1](https://lexplore.info/current-projects/algal-blooms-in-lake-geneva-in-the-face-of-global-changes-alga/) · [Evidence 2](https://github.com/mdugenne/Lexplore_ALGA) |
| [14823](https://ecotaxa.obs-vlfr.fr/prj/14823) | Flowcam tara oceans polar circle ALL LEGS | 1 | 0 | 0 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [15080](https://ecotaxa.obs-vlfr.fr/prj/15080) | Lexplore_ALGA_Flowcam_macro | 190 | 18 | 18 | 官方ALGA精確連ID；來源身分確認，影像條款未確認 | [Evidence 1](https://lexplore.info/current-projects/algal-blooms-in-lake-geneva-in-the-face-of-global-changes-alga/) · [Evidence 2](https://github.com/mdugenne/Lexplore_ALGA) |
| [16271](https://ecotaxa.obs-vlfr.fr/prj/16271) | Great Bay Phytoplankton Timeseries 10x | 1 | 0 | 0 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [17598](https://ecotaxa.obs-vlfr.fr/prj/17598) | Flowcam_IF_MA | 41 | 4 | 6 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [17636](https://ecotaxa.obs-vlfr.fr/prj/17636) | flowcam_sn10630_dy180_biocarbon1_respire | 1 | 0 | 0 | CARTRIDGE/BIO-CARBON來源影像條款未確認；物理海洋資料DOI不能代替 | Source project metadata; no exact image grant located |
| [17686](https://ecotaxa.obs-vlfr.fr/prj/17686) | BCRE_2024 | 1 | 0 | 0 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [17869](https://ecotaxa.obs-vlfr.fr/prj/17869) | 2025-07-21_Casco Bay_10X | 2 | 0 | 0 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [17886](https://ecotaxa.obs-vlfr.fr/prj/17886) | FlowCAM Baltic Pokmark (100 - 250μm) | 88 | 5 | 13 | 來源metadata指Gdansk團隊；作者工具repo不是指定影像授權 | [Evidence 1](https://github.com/makkaktus/FlowCAM_to_EcoTaxa) |
| [17887](https://ecotaxa.obs-vlfr.fr/prj/17887) | FlowCAM Baltic Pokmark (>250μm) | 528 | 50 | 78 | 來源metadata指Gdansk團隊；作者工具repo不是指定影像授權 | [Evidence 1](https://github.com/makkaktus/FlowCAM_to_EcoTaxa) |
| [17935](https://ecotaxa.obs-vlfr.fr/prj/17935) | flowcam_micro_sn10630_jc275_cartridge_Bongo100_tofix | 2,020 | 286 | 243 | CARTRIDGE/BIO-CARBON來源影像條款未確認；物理海洋資料DOI不能代替 | Source project metadata; no exact image grant located |
| [18222](https://ecotaxa.obs-vlfr.fr/prj/18222) | FlowCam_22agosto_Mariaelena | 0 | 1 | 0 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [18329](https://ecotaxa.obs-vlfr.fr/prj/18329) | FlowCam_Abr24_Zooplankton_Md | 14 | 3 | 4 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [19557](https://ecotaxa.obs-vlfr.fr/prj/19557) | Dol-LAYER Project Phytoplankton Samples | 6 | 0 | 1 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [19751](https://ecotaxa.obs-vlfr.fr/prj/19751) | Tara Europa WP2 20µm - Leg1-15 - 100% >=500pix - validated pictures | 45 | 3 | 6 | 相關TaraEuropa CC BY-NC資料集實為project15671/collection310；尚缺同影像對照與範圍核對 | [Evidence 1](https://ipt.data-terra.org/resource?r=tara-europa-flowcam&request_locale=en) · [Evidence 2](https://doi.org/10.15468/2y5vav) |
| [19759](https://ecotaxa.obs-vlfr.fr/prj/19759) | Tara Europa WP2 20µm - for extra indentification - | 258 | 39 | 34 | 相關TaraEuropa CC BY-NC資料集實為project15671/collection310；尚缺同影像對照與範圍核對 | [Evidence 1](https://ipt.data-terra.org/resource?r=tara-europa-flowcam&request_locale=en) · [Evidence 2](https://doi.org/10.15468/2y5vav) |
| [20795](https://ecotaxa.obs-vlfr.fr/prj/20795) | Test Flowcam macro 5mm | 54 | 6 | 3 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [21049](https://ecotaxa.obs-vlfr.fr/prj/21049) | Test 10000 - Flowcam sediment traps astrid ridge - Norwegian Polar Institut | 47 | 3 | 4 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [21146](https://ecotaxa.obs-vlfr.fr/prj/21146) | flowcam_testmacroFabien | 98 | 15 | 9 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [21713](https://ecotaxa.obs-vlfr.fr/prj/21713) | Flowcam sediment traps astrid ridge - Norwegian Polar Institut | 19 | 3 | 4 | 未找到可精確覆蓋此專案影像的來源條款 | Source project metadata; no exact image grant located |
| [22067](https://ecotaxa.obs-vlfr.fr/prj/22067) | microscopic_pandemic_flowcam | 16,907 | 2,094 | 2,124 | 本地metadata指Lake Geneva/Ibelings；公開同團隊Microscopic Pandemic線索，無exact ID/影像條款 | [Evidence 1](https://gleon.org/wp-content/uploads/2026/10/G2026_Abstract-Book.pdf) |

## Material limitations

Some projects are composites or renamed/subsampled derivatives, and corresponding public dataset IDs differ. Their provenance cannot be collapsed into the nearest similarly named public dataset. A specific training-image or original-project mapping may be required to establish the relevant terms. Neither noncommercial packaging nor a disclosure alone supersedes binding third-party contractual restrictions, if any apply. The research unit's model-release consent does not purport to speak for every source provider.

This package contains learned tensors and reviewed model metadata only. A2 received a bounded matched membership-inference check and textual-path/sample-exact-content overlap checks; see [PRIVACY_EVALUATION.md](PRIVACY_EVALUATION.md). No image reconstruction, full content/near-duplicate search, or stronger white-box audit was performed. These questions remain distinct from conversion integrity and source rights.
