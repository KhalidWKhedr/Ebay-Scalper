from typing import Dict, List, Optional

class SiteDomainModel:
    """Model to encapsulate eBay site-domain mappings."""

    def __init__(self, site_domain_mapping: Dict[str, Dict[str, str]]):
        """
        Initialize the model with the site-domain mapping.

        Args:
            site_domain_mapping (Dict[str, Dict[str, str]]): A dictionary mapping site IDs to site and domain information.
        """
        self.site_domain_mapping = site_domain_mapping

    def get_site_names(self) -> List[str]:
        """Retrieve a list of all available site names (e.g., 'eBay United States')."""
        return [site_info["site"] for site_info in self.site_domain_mapping.values()]

    def get_domain_for_site(self, site_name: str) -> Optional[str]:
        """
        Retrieve the domain for a given site name.

        Args:
            site_name (str): The name of the site (e.g., 'eBay United States').

        Returns:
            Optional[str]: The domain associated with the site, or None if not found.
        """
        for site_info in self.site_domain_mapping.values():
            if site_info["site"] == site_name:
                return site_info["domain"]
        return None

    def get_site_id_for_site_name(self, site_name: str) -> Optional[str]:
        """
        Retrieve the site ID for a given site name.

        Args:
            site_name (str): The name of the site (e.g., 'eBay United States').

        Returns:
            Optional[str]: The site ID associated with the site, or None if not found.
        """
        for site_id, site_info in self.site_domain_mapping.items():
            if site_info["site"] == site_name:
                return site_id
        return None

    def get_default_domain(self) -> Optional[str]:
        """
        Retrieve the default domain (e.g., the domain of the first site in the mapping).

        Returns:
            Optional[str]: The default domain, or None if the mapping is empty.
        """
        if not self.site_domain_mapping:
            return None
        return next(iter(self.site_domain_mapping.values()))["domain"]