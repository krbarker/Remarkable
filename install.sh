function setString() {
	local VARNAME="${1}"
	local DEFAULT="${2}"
	if [ -z "${!VARNAME}" ]; then
		eval ${VARNAME}="${DEFAULT}"
	fi
}

# install prefix directory
setString "PREFIX" "/usr"
sudo mkdir -p "${PREFIX}"

# install binary
setString "BIN_DIR" "${PREFIX}/bin"
sudo mkdir -p "${BIN_DIR}"
sudo cp bin/remarkable "${BIN_DIR}"/

# install library directory
setString "LIB_DIR" "${PREFIX}/lib"
sudo mkdir -p "${LIB_DIR}"

# install python packages
setString "PYTHON_DIR" "${LIB_DIR}/python3/dist-packages"
sudo mkdir -p "${PYTHON_DIR}"
sudo cp -R {markdown,pdfkit,remarkable,remarkable_lib} "${PYTHON_DIR}"/
sudo cp debian/*.egg-info "${PYTHON_DIR}"/

# install mime type
setString "MIME_DIR" "${LIB_DIR}/mime/packages"
sudo mkdir -p "${MIME_DIR}"
sudo cp debian/remarkable.mime "${MIME_DIR}"/

# install share directory
setString "SHARE_DIR" "${PREFIX}/share"

# install desktop entry
setString "DESKTOP_DIR" "${SHARE_DIR}/applications"
sudo mkdir -p "${DESKTOP_DIR}"
sudo cp remarkable.desktop "${DESKTOP_DIR}"/

# install documentation
setString "DOC_DIR" "${SHARE_DIR}/doc/remarkable"
sudo mkdir -p "${DOC_DIR}"

# install glib
setString "GLIB_DIR" "${SHARE_DIR}/glib-2.0/schemas"
sudo mkdir -p "${GLIB_DIR}"
sudo cp data/glib-2.0/schemas/* "${GLIB_DIR}"/

# install help
setString "HELP_DIR" "${SHARE_DIR}/help"
sudo mkdir -p "${HELP_DIR}"

# install icon(s)
setString "ICON_DIR" "${SHARE_DIR}/icons/"
sudo mkdir -p "${ICON_DIR}"
setString "ICON_PNG_DIR" "${ICON_DIR}/hicolor/256x256/apps/"
sudo mkdir -p "${ICON_PNG_DIR}"
sudo cp data/media/remarkable.png "${ICON_PNG_DIR}"/
setString "ICON_SVG_DIR" "${ICON_DIR}/hicolor/scalable/apps/"
sudo mkdir -p "${ICON_SVG_DIR}"
sudo cp data/media/remarkable.svg "${ICON_SVG_DIR}"/

# install remarkable data
setString "APP_DIR" "${SHARE_DIR}/remarkable"
sudo mkdir -p "${APP_DIR}"
sudo cp -R data/{media,ui} "${APP_DIR}"/


