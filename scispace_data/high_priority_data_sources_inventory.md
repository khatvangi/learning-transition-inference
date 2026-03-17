## TL;DR

I cannot locate which papers are marked HIGH PRIORITY from the provided context because the Data Availability Assessment column or its flags were not included. To proceed, please supply the list or an export of the assessment column or the paper identifiers flagged HIGH PRIORITY.

----

## Flag status unknown

The query requests an inventory of papers flagged HIGH PRIORITY, but the supplied dataset excerpts do not include any Data Availability Assessment flags or an explicit HIGH PRIORITY label. Therefore, there is insufficient evidence to identify which specific papers should be extracted or to produce the requested per-paper details.

To enable the requested inventory, please provide one of the following: a table or CSV that includes the Data Availability Assessment column with HIGH PRIORITY entries, or a list of DOIs / titles that you consider HIGH PRIORITY. Insufficient evidence

----

## Data extraction template

This section provides a ready-to-use table and field definitions to collect the requested information for each HIGH PRIORITY paper once those papers are specified.

| Field | Description |
|---|---|
| Citation | Full citation including title, authors, journal, year |
| DOI | DOI string |
| Data availability status | Exact wording (e.g., "Supplementary files", repository URL, "data available on request", or notes on figure digitization feasibility) |
| Sample size N individuals | Number of subjects reported |
| Sample size N time points | Number of repeated measurements or trials per subject |
| Trajectory type measured | e.g., song similarity score, accuracy, latency, path efficiency |
| Statistical methods | Named methods used (e.g., changepoint detection, HMM, state-space models) |
| Direct quotes on data/trajectories | Verbatim quotes from the paper about data availability or individual trajectories with page/section |
| Domain | Domain label (Birdsong, Conditioning, Maze, Insight, etc.) |

Guidance for filling template
- **Citation capture**: record the journal-formatted citation and DOI exactly as printed.  
- **Data availability**: copy the paper’s exact wording and any repository URLs; if only figures are available, note **figure digitization** and comment on image resolution.  
- **Sample sizes**: extract the exact Ns from Methods or Results; if Ns differ across analyses, list them separately with labels.  
- **Trajectories and methods**: list the metric name and the explicit statistical methods reported; for changepoint/HMM/state-space, copy the method name used in text.  
- **Direct quotes**: include verbatim lines and cite the section (e.g., Methods, Data availability) to preserve traceability.

----

## Next steps to resolve

To produce the detailed inventory you requested, please supply at least one of the following items so papers flagged HIGH PRIORITY can be unambiguously identified:  
- **Provide assessment export**: CSV or spreadsheet with the Data Availability Assessment column showing HIGH PRIORITY entries.  
- **Provide identifiers**: a list of DOIs or full titles labeled HIGH PRIORITY.  
- **Provide PDFs**: PDFs of the HIGH PRIORITY papers to extract sample sizes, methods, and direct quotes.

After you supply the HIGH PRIORITY list or files, I will populate the template for each paper, extracting DOIs, exact data-availability wording (including repository URLs or supplementary file references), Ns, measured trajectory type, stated statistical methods, and verbatim quotes about data or individual trajectories.