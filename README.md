# EBReg project page

Project website for **Self-Supervised Collapse Prevention with Score-Based Entropy Maximization**, arXiv:2611.11379.

The project uses **EBReg** (Entropy-Based Regularization), matching the paper, figures, presentation, and videos.

Plain HTML, CSS, and JavaScript; no build tools or runtime dependencies. All videos, posters, paper figures, and downloads are hosted locally. Links work under a GitHub Pages repository subpath.

## Preview

From this directory:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000.

## GitHub Pages

Intended destination: `kadarsh22/sereg.github.io`, with site URL `https://kadarsh22.github.io/sereg.github.io/` once deployed.

Push this directory as the repository root on `main`. In repository **Settings → Pages → Build and deployment**, select **GitHub Actions**. The included `.github/workflows/pages.yml` publishes only the website and assets whenever `main` changes. The workflow can also be run manually from **Actions → Deploy project page**.

If you change the repository name or domain, update the canonical URL and Open Graph URL/image in `index.html`.

## Content and assets

- Paper metadata, affiliations, methodology, and reported results: https://arxiv.org/abs/2611.11379 (v1, 8 November 2026).
- `assets/images/method.png`: Figure 2 from the paper, https://arxiv.org/html/2611.11379v1/ebreg_block_diagram.png. Paper attribution: Adarsh Kappiyath, Silpa Vadakkeeveetil Sreelatha, Xiatian Zhu, Yann LeCun, Lu Yin, and Amir Bar. The paper is licensed CC BY 4.0: https://creativecommons.org/licenses/by/4.0/.
- Videos extracted from the supplied `EntropyBasedRegularization-EBREG.pptx`: `ppt/media/media1.mp4` (slide 7, 25 seconds) and `ppt/media/media2.mp4` (slide 25, 60 seconds). Both contain silent H.264 video. Their encoded streams are preserved, with MP4 metadata moved to the beginning for web playback.
- Posters are frames at 23 and 55 seconds, respectively, from those original animations. Both videos include text descriptions on the page and native playback controls; neither autoplays.
- The complete supplied presentation and paper are downloadable under `assets/downloads/`.
- Results reproduce matched comparisons from Table 2 and all-corruption means from Table 5. The page distinguishes percentage-point gains from relative gains.
- The site does not claim that the illustrative animations are measured results or that implementation code has been released.

Edit `index.html` for text and results, `styles.css` for the design, and `script.js` for tabs, navigation, and citation copying. Keep the visible BibTeX and `assets/downloads/ebreg.bib` in sync.

## Verification

Checked in Chrome at widths of 320, 390, 768, and 1440 pixels, including repository-subpath URLs. Both videos play and seek; keyboard tabs, citation copying, local downloads, paper section anchors, and JavaScript-disabled video access were checked. Automated axe checks reported no WCAG 2 A/AA or 2.1 AA violations in the tested mobile state. This is an automated check, not a full accessibility audit.

## Research-page additions

The resource bar labels implementation code **Coming soon**. The introductory summary emphasizes Gaussian smoothing and parametric score learning. The page includes the paper abstract, a comparison with contrastive regularization, VICReg and SIGReg, and conceptual training pseudocode adapted from Appendix C, Algorithm 1.

Sensitivity figures reproduce the six noise-scale and score-update measurements from Table 3 (ResNet-50, ImageNet-1K, one factor varied at a time). Both use the same 55–70% vertical range and highlight the defaults. SVGs include accessible descriptions; PNG exports and the source CSV are downloadable. Regenerate them with `python3 scripts/plot_sensitivity.py` (requires Matplotlib). These figures show sensitivity among tested settings, not ablations that remove either component.

Author links were verified against the authors’ own or institutional pages: [Adarsh Kappiyath](https://kadarsh22.github.io/), [Silpa Vadakkeeveetil Sreelatha](https://vssilpa.github.io/), [Xiatian Zhu’s lab](https://x-up-lab.github.io/), [Yann LeCun](https://yann.lecun.com/), [Lu Yin](https://luuyin.com/), and [Amir Bar](https://www.amirbar.net/). The research-contact address is a.kappiyath@surrey.ac.uk, as supplied by the author.


## Author and affiliation badges

Author badges link to each author’s homepage and preserve the paper’s affiliation numbers. Institution badges link to official homepages. Photos and logos are served locally; their original image data is preserved and fitted into badges with CSS.

Author photo sources:

- Adarsh Kappiyath: https://kadarsh22.github.io/assets/img/prof_pic.jpg
- Silpa Vadakkeeveetil Sreelatha: https://vssilpa.github.io/assets/profile-pics/silpa.jpeg
- Xiatian Zhu: https://x-up-lab.github.io/assets/img/members/xiatian-480.webp
- Yann LeCun: http://yann.lecun.com/ex/images/ylc-thumb.jpeg
- Lu Yin: https://luuyin.com/assets/img/prof_pic_uk.jpg
- Amir Bar: https://pxl01-imperialacuk.terminalfour.net/fit-in/428x572/filters:upscale()/prod01/channel_3/media/imperial-college/faculty-of-engineering/computing/public/website-images/-non-standard-dimensions/Amir-Bar.png (existing WebP thumbnail linked from https://www.imperial.ac.uk/computing/people/academic-staff/)

Institution logo sources:

- University of Surrey: https://www.surrey.ac.uk/favicon.svg?v=v3
- New York University: https://www.nyu.edu/favicon.ico
- AMI Labs: https://cdn.prod.website-files.com/6968f95cf64678111b0f9968/6970a7533cac6b6ee8014af0_webclip.png (linked from https://amilabs.xyz/)
- Shenzhen University of Advanced Technology: https://www.suat-sz.edu.cn/en/images/25/favicon.ico
- Imperial College London: https://www.imperial.ac.uk/assets/website/images/favicon/favicon.svg
