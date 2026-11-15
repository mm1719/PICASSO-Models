# Attribution and source-rights ledger

Prepared for A2, the 20-target classifier. Original datasets and private source exports are not included. Identified source statements and unverified additional-source terms are distinguished below.

## Pretrained model and implementation

- Original ConvNeXt V2 research: Sanghyun Woo, Shoubhik Debnath, Ronghang Hu, Xinlei Chen, Zhuang Liu, In So Kweon, and Saining Xie (2023). [Paper](https://arxiv.org/abs/2301.00808), [official repository](https://github.com/facebookresearch/ConvNeXt-V2).
- timm implementation and model distribution: Ross Wightman and timm contributors. [Exact model](https://huggingface.co/timm/convnextv2_large.fcmae_ft_in22k_in1k).
- Weight license: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/), independently confirmed by the exact timm model card and Meta's [license file](https://github.com/facebookresearch/ConvNeXt-V2/blob/main/LICENSE).
- Preserve attribution and supplied license/copyright/disclaimer notices, link the licensed source and license, and mark modifications. Do not imply upstream endorsement. Do not replace the pretrained-weight conditions with a software-only MIT/Apache claim.
- Modification notice: “PICASSO fine-tunes the upstream pretrained ConvNeXt V2-L backbone for FlowCAM image classification, with a task-specific classifier and 128-pixel training/evaluation configuration. This A2 package has 20 output targets and uses an EMA epoch-40 checkpoint; it is not the R1 historical baseline.”
- The A2 configuration records pretrained initialization from the exact timm model name above. The historical upstream weight revision is not independently pinned in the preserved evidence; no revision-level reproducibility claim is made.
- Upstream copyright: Copyright (c) Meta Platforms, Inc. and affiliates. The complete supplied license/disclaimer notice is preserved in `UPSTREAM-CONVNEXTV2-LICENSE.txt`.

## Six main sources used by A2

The principal source records now all have an identified license. These records document the source releases; they are not a claim that a trained model automatically inherits every dataset license. The noncommercial distribution also follows the independent pretrained-weight NC condition.

| Local source identity | Published source | Verified public rights statement | Evidence and qualification |
|---|---|---|---|
| `life_watch` | [LifeWatch training set, Zenodo v2](https://zenodo.org/records/16679297) | CC BY 4.0 | Direct official [Zenodo API](https://zenodo.org/api/records/16679297), `metadata.license.id = cc-by-4.0` |
| `life_watch_2026_image_library` | [LifeWatch full image library](https://doi.org/10.14284/680) | CC BY 4.0 | [VLIZ IMIS record](https://www.vliz.be/en/imis?module=dataset&dasid=8437) explicitly identifies the license |
| `flowcam_net` | [FlowCAMNet](https://doi.org/10.17882/101961) | CC BY-NC 4.0 | Publisher-deposited [DataCite record](https://api.datacite.org/dois/10.17882/101961); matches [maintainer dataset card](https://huggingface.co/datasets/project-oceania/flowcamnet) |
| `ifremer_srn` | [Ifremer SRN images](https://doi.org/10.17882/113233) | CC BY 4.0 | Publisher-deposited [DataCite record](https://api.datacite.org/dois/10.17882/113233); SEANOE HTML fetch remained unavailable |
| `tara_pacific_deck` | [SEANOE Deck Net release](https://doi.org/10.17882/102697) and [IPT v1.4](https://ipt.data-terra.org/resource?r=tara-pac-flowcam-decknet&v=1.4) | SEANOE metadata: CC BY 4.0; IPT and local v1.4 EML: CC BY-NC 4.0 | [Publisher-deposited DOI metadata](https://api.datacite.org/dois/10.17882/102697) confirms the first statement; preserve both instead of silently treating them as identical. A conservative noncommercial scope accommodates the stated NC condition. |
| `tara_pacific_bongo` | [SEANOE Bongo release](https://doi.org/10.17882/102694) and [IPT](https://ipt.data-terra.org/resource?r=tara-pac-flowcam-bongo) | CC BY 4.0 | [Publisher-deposited DOI metadata](https://api.datacite.org/dois/10.17882/102694), local source EML v1.1, and current IPT v1.2 agree |

The Tara provenance was additionally connected through the public EcoTaxa project-collection API: projects 11341/11353 map to collection 314 (Deck Net); 11369/11370 map to collection 320 (Bongo). The detailed collection endpoints returned 403, so the rights statements above rely on the published DOI/IPT records, not an unseen collection page.

## Source creator credits

- **life_watch**: Decrop, Wout; Lagaisse, Rune; Mortelmans, Jonas; Muyle, Julie; Amadei Martínez, Luz; Deneudt, Klaas. LifeWatch observatory data: phytoplankton annotated trainingset by FlowCam imaging in the Belgian Part of the North Sea. [Official metadata](https://zenodo.org/api/records/16679297).
- **flowcam_net**: Jalabert, Laetitia; Signoret, Guillaume; Caray-Counil, Louis; Vilain, Marion; Martins, Emmanuelle; Lombard, Fabien; Picheral, Marc; Irisson, Jean-Olivier. FlowCAMNet : plankton images captured with the FlowCAM. [Official metadata](https://api.datacite.org/dois/10.17882/101961).
- **ifremer_srn**: Wacquet, Guillaume; Lefebvre, Alain. FlowCam images (4X) of Pseudo-nitzschia spp. and Phaeocystis globosa in the English Channel and North Sea. [Official metadata](https://api.datacite.org/dois/10.17882/113233).
- **tara_pacific_deck**: Mériguet, Zoé; Bourdin, Guillaume; Jalabert, Laetitia; Bun, Olivier; Caray--Counil, Louis; Elineau, Amanda; Gorsky, Gaby; Lombard, Fabien. Global scale surface micro-plankton dataset collected with Deck Net and imaged with FlowCam during the Tara Pacific Expedition. [Official metadata](https://api.datacite.org/dois/10.17882/102697).
- **tara_pacific_bongo**: Mériguet, Zoé; Kristan, Nathaniel; Bourdin, Guillaume; Gorsky, Gaby; Karp-Boss, Lee; Lombard, Fabien. Global scale surface micro-plankton dataset collected with Bongo nets and imaged with FlowCam during the Tara Pacific Expedition. [Official metadata](https://api.datacite.org/dois/10.17882/102694).
- **LifeWatch full image library**: Rune Lagaisse, Luz Amadei Martinez, Wout Decrop, Klaas Deneudt, Julie Muyle, Jonas Mortelmans, and Flanders Marine Institute (VLIZ). [Source and supplied citation](https://www.vliz.be/en/imis?module=dataset&dasid=8437).
- Preserve the Tara Pacific Consortium credit from the IPT citation in addition to the DOI's creator fields. SEANOE and IPT list credits in different orders; do not overwrite either source-native citation.
- EcoTaxa tool credit: Marc Picheral, Samuel Colin, and Jean-Olivier Irisson. [EcoTaxa](https://ecotaxa.obs-vlfr.fr/). This software/platform credit does not replace attribution to individual datasets and rights holders.


## Additional EcoTaxa source credits and uncertainty

A2 additionally used 48 EcoTaxa projects, with a combined 45,734 training, 5,741 validation, and 5,735 test rows. [DATA_PROVENANCE.md](DATA_PROVENANCE.md) preserves project titles, source links, counts, and the specific evidence available for each project. The individual dataset creators retain their respective rights; EcoTaxa platform credit is not a substitute for dataset credit.

For project 6015, the exact source is **Coastal Cabo Frio Upwelling Plankton community analyzed with FlowCam**, [VLIZ/IMIS dataset 8058](https://www.vliz.be/en/imis?dasid=8058&module=dataset), with a CC BY 4.0 statement and image coverage. Source-listed credits: Lohengrin F., Moura L., Guilherme C., Reis C., Matos T., Figueredo B., and Coutinho R.; IEAPM, Brazilian Navy. All 3,183 A2 rows from this project matched the preserved export metadata and the official spatial, temporal, and instrument scope. No DOI from a different Cabo Frio instrument or dataset is substituted.

For the other 47 additional projects, precise snapshot-specific image terms were not independently established. Related papers, analytical tables, source-code repositories, public project access, and funder policies are not represented as licenses on the exact source images. A former provisional local display policy is not used as rights evidence. This disclosure does not assert either that the data were unauthorized or that all third-party rights are cleared. See the model card for the distinction between training-data rights and learned-weight distribution.

## Package scope

PICASSO's task-specific fine-tuning and this A2 weight package are credited to [mm1719](https://github.com/mm1719). Modifications include a task-specific 20-target classifier, fine-tuning on the recorded FlowCAM sources, and 128-pixel evaluation. The safe-format conversion preserves the EMA epoch-40 tensor values; verification is reported separately.

Original source datasets retain their own terms. The pretrained weights independently impose the noncommercial condition. No images, per-image manifests, personal contact details, credentials, or local acquisition scripts are distributed. The weight license does not clear rights that the distributor cannot grant.

Preserve this attribution, license text/link, change notices, and supplied disclaimers when sharing or adapting the weights as required by CC BY-NC 4.0. No upstream author or data-provider endorsement is implied.
