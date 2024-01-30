import untangle
import os, pathlib


def main():
    root_file = pathlib.Path(__file__).parent.resolve()
    xml_path = os.path.join(root_file, "statics", "en.xml")

    obj = untangle.parse(xml_path)
    groups = obj.languagePack.language.group
    for group in groups:
        print(group["target"])
        if group["target"] == "view":
            for row in group.item:
                print(f"\t{row.cdata}")

    # common
    # button
    # error
    # message
    # panel
    # view
    #         View
    #         View mode:
    #         Thumbnails
    #         Text list
    #         images/page
    #         Are you sure you wish to remove this file?
    #         Keyboard shortcut: SPACE,N,RIGHTARROW,PAGE DOWN
    #         Keyboard shortcut: P,LEFTARROW,PAGE UP
    #         Dimensions
    #         Are you sure you wish to remove this from your favorites list?
    # createdir
    # upload
    # edit_image
    # tinymce
    # favorites
    # history


if __name__ == '__main__':
    main()