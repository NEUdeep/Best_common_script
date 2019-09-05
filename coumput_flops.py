#计算3D网络的flops；nn.Conv3d
% Matlab Code
% FLOPs for nn.Conv3d, without bias
A_size = [num_out/group, prod(kernel)*num_input/group];       % weight
C_size = [prod(kernel)*num_input/group, out_h*out_w*out_t];   % im2col
flops = 0;
for i_group = 1:group    
    flops = flops + A_size(1)*A_size(2)*C_size(2);
end