FROM openmicroscopy/omero-server:5

RUN ["wget", "-P", "/opt/omero/server/OMERO.server/lib/server", "https://artifacts.glencoesoftware.com/artifactory/gs-omero-snapshots-local/com/glencoesoftware/omero/omero-zarr-pixel-buffer/0.4.1/omero-zarr-pixel-buffer-0.4.1.jar"]
RUN ["wget", "-P", "/opt/omero/server/OMERO.server/lib/server", "https://repo1.maven.org/maven2/com/github/ben-manes/caffeine/caffeine/3.1.8/caffeine-3.1.8.jar"]
RUN ["wget", "-P", "/opt/omero/server/OMERO.server/lib/server", "https://repo1.maven.org/maven2/dev/zarr/jzarr/0.4.2/jzarr-0.4.2.jar"]
RUN ["wget", "-P", "/opt/omero/server/OMERO.server/lib/server", "https://repo1.maven.org/maven2/org/lasersonlab/s3fs/2.2.3/s3fs-2.2.3.jar"]
RUN ["wget", "-P", "/opt/omero/server/OMERO.server/lib/server", "https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-s3/1.12.659/aws-java-sdk-s3-1.12.659.jar"]
