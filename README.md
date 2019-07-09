# TCGA_Data_Download

This package provides utility to download data, meta-data from TCGA

##  GDC Model
Each entity in the GDC has a set of properties and links.

### Properties
**Type** is a required property for all entities. Entity types include project, case, demographic, sample, read_group and others

**System properties** are properties used in GDC system operation and maintenance. They cannot be modified except under special circumstances.

**Unique keys** are properties, or combinations of properties, that can be used to uniquely identify the entity in the GDC. For example, the tuple (combination) of [ project_id, submitter_id ] is a unique key for most entities, which means that although submitter_id does not need to be unique in GDC, it must be unique within a project. See GDC Identifiers below for details.

### Links
Links define relationships between entities, and the multiplicity of those relationships (e.g. one-to-one, one-to-many, many-to-many).