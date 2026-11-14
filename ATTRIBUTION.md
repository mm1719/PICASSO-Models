# Attribution and source-rights ledger

Verified for the R1 historical baseline release. Original datasets, private source exports, and A2 weights are not included.

## Pretrained model and implementation

- Original ConvNeXt V2 research: Sanghyun Woo, Shoubhik Debnath, Ronghang Hu, Xinlei Chen, Zhuang Liu, In So Kweon, and Saining Xie (2023). [Paper](https://arxiv.org/abs/2301.00808), [official repository](https://github.com/facebookresearch/ConvNeXt-V2).
- timm implementation and model distribution: Ross Wightman and timm contributors. [Exact model](https://huggingface.co/timm/convnextv2_large.fcmae_ft_in22k_in1k).
- Weight license: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/), independently confirmed by the exact timm model card and Meta's [license file](https://github.com/facebookresearch/ConvNeXt-V2/blob/main/LICENSE).
- Preserve attribution and supplied license/copyright/disclaimer notices, link the licensed source and license, and mark modifications. Do not imply upstream endorsement. Do not replace the pretrained-weight conditions with a software-only MIT/Apache claim.
- Modification notice: “PICASSO fine-tunes the upstream pretrained ConvNeXt V2-L backbone for FlowCAM image classification, with a task-specific classifier and 128-pixel training/evaluation configuration. This R1 release has 23 output targets. It is not the A2 application checkpoint.”
- The R1 configuration records pretrained initialization from the exact timm model name above. The historical upstream weight revision is not independently pinned in the preserved evidence; no revision-level reproducibility claim is made.
- Upstream copyright: Copyright (c) Meta Platforms, Inc. and affiliates. The complete supplied license/disclaimer notice is preserved in `UPSTREAM-CONVNEXTV2-LICENSE.txt`.

## Six main sources used by R1

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


## Release scope

PICASSO's task-specific fine-tuning and this R1 weight distribution are credited to [mm1719](https://github.com/mm1719). Modifications include a task-specific classifier, training on the six recorded FlowCAM sources, and 128-pixel evaluation. The release is a tensor-only safetensors conversion of the EMA epoch-27 R1 checkpoint; all tensor values are unchanged by packaging.

Original source datasets retain their own licenses. Dataset attribution here does not claim that download access alone is authorization, or that source licenses automatically attach to all learned parameters. The pretrained weights independently impose the noncommercial condition. No images, per-image manifests, credentials, or local acquisition scripts are distributed.

Preserve this attribution, the license link/text, change notices, and supplied disclaimers when sharing or adapting the weights as required by CC BY-NC 4.0. No upstream author or data-provider endorsement is implied.
