---
title: GA4GH
page_id: ga4gh
type: technologies_standards
contributors: [Marion Shadbolt]
description: The Global Alliance for Genomics and Health is a policy-framing and technical standards-setting organization, seeking to enable responsible genomic data sharing within a human rights framework.
affiliations: [GA4GH]
datatable: true
---

An overview of selected GA4GH data standards, see [GA4GH website](https://www.ga4gh.org/how-we-work/workstreams/) for all standards.

{% tool "passports" %}
{% tool "beacon" %}

<div class="table-responsive mt-4 mb-5">
  <table>
    <thead>
      <tr>
        <th>Standard
        </th>
        <th>Description
        </th>
        <th>Workstream
        </th>
        <th>version / status
        </th>
        <th>docs
        </th>
        <th>github
        </th>
        <th>publication
        </th>
        <th>other resources
        </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Phenopackets
        </td>
        <td>Define and share individual characteristics, demographics and phenotypes in a standard format
        </td>
        <td><a href="https://ga4gh-cp.github.io/">Clin/Pheno</a>
        </td>
        <td>2.0.0
        </td>
        <td><a href="https://phenopacket-schema.readthedocs.io/en/latest/"><i class="fa-solid fa-book fa-2x"></i></a>
        </td>
        <td><a href="https://github.com/phenopackets/phenopacket-schema"><i class="fa-brands fa-github fa-2x"></i></a>
        </td>
        <td><a href="https://www.nature.com/articles/s41587-022-01357-4"><i class="fa-regular fa-file-lines"></i> Jacobsen et al. 2022</a><br />
            <a href="https://onlinelibrary.wiley.com/doi/abs/10.1002/ggn2.202200016"> <i class="fa-regular fa-file-lines"></i> Ladewig et al. 2022</a>
        </td>
        <td><a href="https://www.iso.org/standard/79991.html"><i class="fa-solid fa-arrow-up-right-from-square"></i> ISO </a>
        </td>
      </tr>
      <tr>
        <td>Beacon
        </td>
        <td>Query across cohort, individual and variant metadata
        </td>
        <td><a href="https://ga4gh-discovery.github.io/">Discovery</a>
        </td>
        <td>2.0.0
        </td>
        <td><a href="http://docs.genomebeacons.org/"><i class="fa-solid fa-book fa-2x"></i></a>
        </td>
        <td><a href="https://github.com/ga4gh-beacon/beacon-v2"><i class="fa-brands fa-github fa-2x"></i></a>
        </td>
        <td><a href="https://onlinelibrary.wiley.com/doi/abs/10.1002/humu.24369"> <i class="fa-regular fa-file-lines"></i> Rambla et al. 2022</a> <br />
            <a href="https://doi.org/10.1093/bioinformatics/btac568"><i class="fa-regular fa-file-lines"></i> Rueda et al. 2022</a>
        </td>
        <td><a href="https://b2ri-documentation.readthedocs.io/en/latest/"> <i class="fa-solid fa-book"></i> Beacon RI</a>
        </td>
      </tr>
      <tr>
        <td>Pedigree
        </td>
        <td>Characterise familial relationships
        </td>
        <td><a href="https://ga4gh-cp.github.io/">Clin/Pheno</a>
        </td>
        <td>under review
        </td>
        <td><a href="https://pedigree.readthedocs.io/en/latest/"><i class="fa-solid fa-book fa-2x"></i></a>
        </td>
        <td>
        </td>
        <td>
        </td>
        <td>
        </td>
      </tr>
      <tr>
        <td>VRS Variation representation 
        </td>
        <td>Characterise variants in a standard format.
        </td>
        <td><a href="https://ga4gh-gks.github.io/">Genomic Knowledge Standards</a>
        </td>
        <td>1.2
        </td>
        <td><a href="https://vrs.ga4gh.org/en/stable/"><i class="fa-solid fa-book fa-2x"></i></a>
        </td>
        <td><a href="https://github.com/ga4gh/vrs"><i class="fa-brands fa-github fa-2x"></i></a>
        </td>
        <td><a href="https://www.sciencedirect.com/science/article/pii/S2666979X21000343"><i class="fa-regular fa-file-lines"></i> Wagner et al. 2021</a>
        </td>
        <td><a href="https://github.com/ga4gh/vrs-python"><i class="fa-brands fa-github"></i> vrs-python</a>
        </td>
      </tr>
      <tr>
        <td>DRS Data repository service
        </td>
        <td>Protocol for accessing data files
        </td>
        <td><a href="https://github.com/ga4gh/wiki/wiki">Cloud</a>
        </td>
        <td>1.2.0
        </td>
        <td><a href="https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.0.0/docs/"><i class="fa-solid fa-book fa-2x"></i></a>
        </td>
        <td><a href="https://github.com/ga4gh/data-repository-service-schemas"><i class="fa-brands fa-github fa-2x"></i></a>
        </td>
        <td>
        </td>
        <td>
        </td>
      </tr>
      <tr>
        <td>WES Workflow Execution Service
        </td>
        <td>API to enable users to submit workflow requests to workflow execution systems
        </td>
        <td><a href="https://github.com/ga4gh/wiki/wiki">Cloud</a>
        </td>
        <td>1.0.1
        </td>
        <td><a href="https://ga4gh.github.io/workflow-execution-service-schemas/docs/"><i class="fa-solid fa-book fa-2x"></i></a>
        </td>
        <td> <a href="https://github.com/ga4gh/workflow-execution-service-schemas "><i class="fa-brands fa-github fa-2x"></i></a>
        </td>
        <td>
        </td>
        <td> <a href="https://github.com/ga4gh/ga4gh-starter-kit-wes"><i class="fa-brands fa-github"></i>wes starter kit</a>
        </td>
      </tr>
      <tr>
        <td>Passports
        </td>
        <td>Protocol for defining tokens for data access
        </td>
        <td><a href="https://ga4gh-duri.github.io/">DURI</a>
        </td>
        <td> 1.2
        </td>
        <td> <a href="https://github.com/ga4gh-duri/ga4gh-duri.github.io/blob/master/researcher_ids/ga4gh_passport_v1.md"><i class="fa-solid fa-book fa-2x"></i></a>
        </td>
        <td>
        </td>
        <td> <a href="https://doi.org/10.1016/j.xgen.2021.100030"><i class="fa-regular fa-file-lines"></i> Voisin et al. 2021</a>
        </td>
        <td> <a href="https://github.com/ga4gh/ga4gh-starter-kit-passport-ui"><i class="fa-brands fa-github"></i> ui starter kit</a><br>
             <a href="https://github.com/ga4gh/ga4gh-starter-kit-passport-broker"><i class="fa-brands fa-github"></i> broker starter kit</a>
        </td>
      </tr>
      <tr>
        <td>DUO: Data Use Ontology
        </td>
        <td>Translates consent form clause to machine readable ontology
        </td>
        <td><a href="https://ga4gh-duri.github.io/">DURI</a>
        </td>
        <td> 2021-02-23
        </td>
        <td><a href="https://github.com/EBISPOT/DUO"><i class="fa-solid fa-book fa-2x"></i></a>
        </td>
        <td><a href="https://github.com/EBISPOT/DUO"><i class="fa-brands fa-github fa-2x"></i></a>
        </td>
        <td><a href="https://doi.org/10.1016/j.xgen.2021.100028"><i class="fa-regular fa-file-lines"></i> Lawson et al. 2021</a>
        </td>
        <td><a href="https://www.ebi.ac.uk/ols/ontologies/duo"><i class="fa-solid fa-arrow-up-right-from-square"></i> OLS</a>
        </td>
      </tr>
    </tbody>
  </table>
</div>
