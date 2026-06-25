from nplinker import NPLinker

def main():
    # 1. Create an instance of NPLinker using your TOML
    npl = NPLinker("nplinker.toml")

    # 2. Load all data (antiSMASH + GNPS + mappings)
    npl.load_data()

    # 3. Inspect what was loaded
    print("Number of BGCs:", len(npl.bgcs))
    print("Number of GCFs:", len(npl.gcfs))
    print("Number of spectra:", len(npl.spectra))
    print("Number of molecular families:", len(npl.mfs))
    print("Number of strains:", len(npl.strains))

    # 4. Compute links for the first 3 GCFs using Metcalf scoring
    if len(npl.gcfs) > 0 and len(npl.spectra) > 0:
        link_graph = npl.get_links(npl.gcfs[:3], "metcalf")

        # 5. Inspect some links
        print("Number of links in link_graph:", len(link_graph.links))
        print("First few links:", list(link_graph.links)[:5])

        # 6. Get link data between first GCF and first spectrum
        ld = link_graph.get_link_data(npl.gcfs[0], npl.spectra[0])
        print("Link data for first GCF–spectrum pair:", ld)

        # 7. Optionally save everything to a pickle
        npl.save_data("npl.pkl", link_graph)
    else:
        print("Not enough GCFs or spectra to compute links.")

if __name__ == "__main__":
    main()