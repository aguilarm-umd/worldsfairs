.response.docs |
map(
    {
        key: .identifier[] | select(contains("umd")),
        value: (
            "https://iiif.lib.umd.edu/viewer/1.2.0/mirador.html?manifest=fcrepo:dc:2024:5::" +
            (.id | split("/").[-1]) +
            "&iiifURLPrefix=https%3A%2F%2Fiiif.lib.umd.edu%2Fmanifests%2F"
        )
    }
) |
from_entries
