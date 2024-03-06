### ggseg parcellation rda file conversion to csv

setwd('/Users/to8050an/Documents/GitHub/brainsurfy')

load('brainsurfy/atlases/schaefer7_400.rda')

name = schaefer7_400[["atlas"]]
type = schaefer7_400[["type"]]
data = schaefer7_400[["data"]]
palette = schaefer7_400[["palette"]]

atlas = schaefer7_400
atlas_fname = 'schaefer7_400.csv'

get_geometry_points <- function(geometry) {
  if (is.matrix(geometry) || is.data.frame(geometry)) {
    return(geometry)
  }
  if (is.list(geometry)) {
    points_list <- lapply(geometry, get_geometry_points)
    return(do.call(rbind, points_list))
  }
  return(NULL)
}

roi_data <- data.frame()
for (i in 1:length(atlas$data$geometry)) {
  roi_polygons <- data.frame(get_geometry_points(atlas$data$geometry[i]))
  roi_polygons$region <- atlas$data$region[i]
  roi_polygons$hemi <- atlas$data$hemi[i]
  roi_polygons$roi <- atlas$data$roi[i]
  roi_polygons$side <- atlas$data$side[i]
  roi_data <- rbind(roi_data, roi_polygons)
}

write.csv(roi_data, atlas_fname)