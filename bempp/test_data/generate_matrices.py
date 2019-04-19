# Script to be run with legacy Bempp to generate the comparison data.

import bempp.api
import numpy as np

bempp.api.enable_console_logging()

parameters = bempp.api.global_parameters
parameters.assembly.boundary_operator_assembly_type = "dense"
parameters.assembly.potential_operator_assembly_type = "dense"

regular_order = 4
singular_order = 6

parameters.quadrature.near.double_order = regular_order
parameters.quadrature.near.single_order = regular_order
parameters.quadrature.medium.double_order = regular_order
parameters.quadrature.medium.single_order = regular_order 
parameters.quadrature.far.double_order = regular_order
parameters.quadrature.far.single_order = regular_order

parameters.quadrature.double_singular = singular_order

grid = bempp.api.import_grid("sphere.msh")

p0 = bempp.api.function_space(grid, "DP", 0)
dp1 = bempp.api.function_space(grid, "DP", 1)
p1 = bempp.api.function_space(grid, "P", 1)

def generate_bem_matrix(dual_to_range, domain, fname, operator, wavenumber=None):
    """Generate test matrix."""
    print("Generating " + fname)

    if wavenumber is None:
        mat = operator(domain, domain, dual_to_range).weak_form().A
    else:
        mat = operator(domain, domain, dual_to_range, wavenumber).weak_form().A
    np.save(fname, mat)


print("Generating Laplace BEM matrices.")

generate_bem_matrix(
    p0,
    p0,
    "laplace_single_layer_boundary_p0_p0",
    bempp.api.operators.boundary.laplace.single_layer,
)

generate_bem_matrix(
    p0,
    dp1,
    "laplace_single_layer_boundary_p0_dp1",
    bempp.api.operators.boundary.laplace.single_layer,
)

generate_bem_matrix(
    dp1,
    p0,
    "laplace_single_layer_boundary_dp1_p0",
    bempp.api.operators.boundary.laplace.single_layer,
)
generate_bem_matrix(
    dp1,
    dp1,
    "laplace_single_layer_boundary_dp1_dp1",
    bempp.api.operators.boundary.laplace.single_layer,
)
generate_bem_matrix(
    p1,
    p1,
    "laplace_single_layer_boundary_p1_p1",
    bempp.api.operators.boundary.laplace.single_layer,
)

generate_bem_matrix(
    p1,
    p1,
    "laplace_double_layer_boundary",
    bempp.api.operators.boundary.laplace.double_layer,
)

generate_bem_matrix(
    p1,
    p1,
    "laplace_adj_double_layer_boundary",
    bempp.api.operators.boundary.laplace.adjoint_double_layer,
)

generate_bem_matrix(
    p1,
    p1,
    "laplace_hypersingular_boundary",
    bempp.api.operators.boundary.laplace.hypersingular,
)

################################

print("Generating Helmholtz BEM matrices.")

wavenumber = 2.5

generate_bem_matrix(
    p0,
    p0,
    "helmholtz_single_layer_boundary_p0_p0",
    bempp.api.operators.boundary.helmholtz.single_layer,
)

generate_bem_matrix(
    p0,
    dp1,
    "laplace_single_layer_boundary_p0_dp1",
    bempp.api.operators.boundary.laplace.single_layer,
)

generate_bem_matrix(
    dp1,
    p0,
    "laplace_single_layer_boundary_dp1_p0",
    bempp.api.operators.boundary.laplace.single_layer,
)
generate_bem_matrix(
    dp1,
    dp1,
    "laplace_single_layer_boundary_dp1_dp1",
    bempp.api.operators.boundary.laplace.single_layer,
)
generate_bem_matrix(
    p1,
    p1,
    "laplace_single_layer_boundary_p1_p1",
    bempp.api.operators.boundary.laplace.single_layer,
)

generate_bem_matrix(
    p1,
    p1,
    "laplace_double_layer_boundary",
    bempp.api.operators.boundary.laplace.double_layer,
)

generate_bem_matrix(
    p1,
    p1,
    "laplace_adj_double_layer_boundary",
    bempp.api.operators.boundary.laplace.adjoint_double_layer,
)

generate_bem_matrix(
    p1,
    p1,
    "laplace_hypersingular_boundary",
    bempp.api.operators.boundary.laplace.hypersingular,
)