class Company:
    """
    A class with all the variables of a company from the dataset.
    """

    def __init__(self,
            zip_code,
            city,
            address,
            addresses,
            company_name,
            business_registry_number,
            bank_account_number,
            IBAN_number,
            tax_number,
            phone_number,
            secondary_phone_numbers,
            email_address,
            secondary_email_addresses,
            logo,
            social_media_types,
            social_media_profiles,
            subdomain,
            domain,
            linked_subdomains,
            IP_address,
            IPv6_address,
            DNS_NS_domain,
            DNS_MX_domain,
            DNS_TXT,
            DNSSEC,
            SSL_certificate,
            SSL_issuer_organization,
            SSL_issuer_common_name,
            SSL_start_date,
            SSL_end_date,
            SSL_RSA_key_length,
            SSL_algorithm,
            SSL_type_open_ports,
            alternative_IP_address,
            DNS_NS_nameservers
            ):
        self.zip_code = zip_code
        self.city = city
        self.address = address
        self.addresses = addresses
        self.company_name = company_name
        self.business_registry_number = business_registry_number
        self.bank_account_number = bank_account_number
        self.IBAN_number = IBAN_number
        self.tax_number = tax_number
        self.phone_number = phone_number
        self.secondary_phone_numbers = secondary_email_addresses
        self.email_address = email_address
        self.secondary_email_addresses = secondary_email_addresses
        self.logo = logo
        self.social_media_types = social_media_types
        self.social_media_profiles = social_media_profiles
        self.subdomain = subdomain
        self.domain = domain
        self.linked_subdomains = linked_subdomains
        self.IP_address = IP_address
        self.IPv6_address = IPv6_address
        self.DNS_NS_domain = DNS_NS_domain
        self.DNS_MX_domain = DNS_MX_domain
        self.DNS_TXT = DNS_TXT
        self.DNSSEC = DNSSEC
        self.SSL_certificate = SSL_certificate
        self.SSL_issuer_organization = SSL_issuer_organization
        self.SSL_issuer_common_name = SSL_issuer_common_name
        self.SSL_start_date = SSL_start_date
        self.SSL_end_date = SSL_end_date
        self.SSL_RSA_key_length = SSL_RSA_key_length
        self.SSL_algorithm = SSL_algorithm
        self.SSL_type_open_ports = SSL_type_open_ports
        self.alternative_IP_address = alternative_IP_address
        self.DNS_NS_nameservers = DNS_NS_nameservers



