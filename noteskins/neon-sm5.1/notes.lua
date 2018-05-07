local skin_name= Var("skin_name")
return function(button_list, stepstype)
	local rots= {Left= 90, Down= 0, Up= 180, Right= 270}
	local hold_flips= {
		Left= "TexCoordFlipMode_None", Right= "TexCoordFlipMode_None",
		Down= "TexCoordFlipMode_None", Up= "TexCoordFlipMode_None"
	}
	local roll_flips= {
		Left= "TexCoordFlipMode_None", Right= "TexCoordFlipMode_None",
		Down= "TexCoordFlipMode_None", Up= "TexCoordFlipMode_None"
	}
	local rev_hold_flips= {
		Left= "TexCoordFlipMode_None", Right= "TexCoordFlipMode_None",
		Down= "TexCoordFlipMode_None", Up= "TexCoordFlipMode_None"
	}
	local rev_roll_flips= {
		Left= "TexCoordFlipMode_None", Right= "TexCoordFlipMode_None",
		Down= "TexCoordFlipMode_None", Up= "TexCoordFlipMode_None"
	}
	local hold_length= {
		start_note_offset= -0.5,
		end_note_offset= 0.5,
		head_pixs= 32,
		body_pixs= 128,
		tail_pixs= 32,
	}
	
	local roll_length= {
		start_note_offset= -0.5,
		end_note_offset= 0.5,
		head_pixs= 32,
		body_pixs= 265,
		tail_pixs= 32,
	}
	
	local parts_per_beat= 48
	local tap_texture_map= {
		parts_per_beat= parts_per_beat, quanta= {
			{per_beat= 1, trans_x= 0, trans_y= 0},
			{per_beat= 2, trans_x= 0.03125, trans_y= 0},
			{per_beat= 3, trans_x= 0.03125*2, trans_y= 0},
			{per_beat= 4, trans_x= 0.03125*3, trans_y= 0},
			{per_beat= 6, trans_x= 0.03125*4, trans_y= 0},
			{per_beat= 8, trans_x= 0.03125*5, trans_y= 0},
			{per_beat= 12, trans_x= 0.03125*6, trans_y= 0},
			{per_beat= 16, trans_x= 0.03125*7, trans_y= 0},
		},
	}
	local mine_texture_map= {
		parts_per_beat= parts_per_beat, quanta= {
			{per_beat= 1, trans_x= 0, trans_y= 0},
		},
	}
	local hold_active_state_map= {
		parts_per_beat= parts_per_beat, quanta= {
			{per_beat= 1, states= {1}},
		},
	}
	local hold_inactive_state_map= {
		parts_per_beat= parts_per_beat, quanta= {
			{per_beat= 1, states= {2}},
		},
	}
	local roll_active_state_map= {
		parts_per_beat= parts_per_beat, quanta= {
			{per_beat= 1, states= {1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4}},
		},
	}
	local roll_inactive_state_map= {
		parts_per_beat= parts_per_beat, quanta= {
			{per_beat= 1, states= {5}},
		},
	}
	local columns= {}
	for i, button in ipairs(button_list) do
		local hold_tex= "Hold 2x1.png"
		local roll_tex= "Roll 5x1.png"
		columns[i]= {
			width= 64,
			anim_time= 2,
			anim_uses_beats= true,
			padding= 0,
			taps= {
				NoteSkinTapPart_Tap= {
					texture_map= tap_texture_map,
					actor= Def.Model {
						Meshes="tap note model.txt",
						Materials="tap note model.txt",
						Bones="tap note model.txt",
						InitCommand= function(self) self:rotationz(rots[button]) end}},
				NoteSkinTapPart_Mine= {
					texture_map= tap_texture_map,
					actor= Def.Model {
						InitCommand= function(self) self:effectclock("beat"):spin():effectmagnitude(0,0,45) end,
						Meshes="mine model.txt",
						Materials="mine model.txt",
						Bones="mine model.txt"}},
				NoteSkinTapPart_Lift= { -- fuck lifts
					texture_map= tap_texture_map,
					actor= Def.Model {
						InitCommand= function(self) self:effectclock("beat") end,
						Meshes="lift model.txt",
						Materials="lift model.txt",
						Bones="lift model.txt"}},
			},
			holds= {
				TapNoteSubType_Hold= {
					{
						state_map= hold_inactive_state_map,
						textures= {hold_tex},
						flip= hold_flips[button],
						length_data= hold_length,
					},
					{
						state_map= hold_active_state_map,
						textures= {hold_tex},
						flip= hold_flips[button],
						length_data= hold_length,
					},
				},
				TapNoteSubType_Roll= {
					{
						state_map= roll_inactive_state_map,
						textures= {roll_tex},
						flip= roll_flips[button],
						length_data= roll_length,
					},
					{
						state_map= roll_active_state_map,
						textures= {roll_tex},
						flip= roll_flips[button],
						length_data= roll_length,
					},
				},
			},
			reverse_holds= {
				TapNoteSubType_Hold= {
					{
						state_map= hold_inactive_state_map,
						textures= {hold_tex},
						flip= rev_hold_flips[button],
						length_data= hold_length,
					},
					{
						state_map= hold_active_state_map,
						textures= {hold_tex},
						flip= rev_hold_flips[button],
						length_data= hold_length,
					},
				},
				TapNoteSubType_Roll= {
					{
						state_map= roll_inactive_state_map,
						textures= {roll_tex},
						flip= rev_roll_flips[button],
						length_data= roll_length,
					},
					{
						state_map= roll_active_state_map,
						textures= {roll_tex},
						flip= rev_roll_flips[button],
						length_data= roll_length,
					},
				},
			},
		}
	end
	return {
		columns= columns,
		vivid_operation= false, -- output 200%
	}
end
