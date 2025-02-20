import omero
import omero.cli
import argparse
from omero.model import ExternalInfoI

def main(args):
    path = args.path
    image_id = args.image_id

    with omero.cli.cli_login() as c:    
        conn = omero.gateway.BlitzGateway(client_obj=c.get_client())
        img = conn.getObject("Image", image_id)
        info = ExternalInfoI()
        info.entityType = omero.rtypes.rstring("com.glencoesoftware.ngff:multiscales")
        info.entityId =  omero.rtypes.rlong(3)
        info.lsid = omero.rtypes.rstring(path)
        img.details.externalInfo = info
        img = conn.getUpdateService().saveAndReturnObject(img._obj)
        print(f"Image {image_id} updated with external info\n{pretty_extinf(img.details.externalInfo)}")


def pretty_extinf(extinf):
    res = f"[ entityType: {extinf.entityType._val}\n"
    res += f"entityId: {extinf.entityId._val}\n"
    res += f"lsid: {extinf.lsid._val} ] "
    return res


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Set external info for an OMERO image')
    parser.add_argument('image_id', type=int, help='ID of the OMERO image')
    parser.add_argument('path', type=str, help='Path to the zarr file')
    args = parser.parse_args()
    main(args)
