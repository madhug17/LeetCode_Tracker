from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import datetime

# Generate private key
key = rsa.generate_private_key(
    public_exponent=65537, # more number more secure , right now our thing is stable man 
    key_size=2048, # How strong the encryption is
)

# Write private key
with open("key.pem", "wb") as f:
    f.write(
        key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )

# Generate self-signed certificate
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "IN"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Telangana"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "Hyderabad"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Leetcode Tracker"),
    x509.NameAttribute(NameOID.COMMON_NAME, "localhost"), # the certificates only belongs to the local host only man 
])

cert = (
    x509.CertificateBuilder() # this will create the certificates man 
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.datetime.utcnow())
    .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
    .add_extension(
        x509.SubjectAlternativeName([x509.DNSName("localhost")]),
        critical=False,
    )
    .sign(key, hashes.SHA256())
)

# Write certificate
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("SSL certificate generated successfully!")