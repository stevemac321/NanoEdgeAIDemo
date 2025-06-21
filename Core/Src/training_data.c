#include <stddef.h>


float training_data[5][140] = {
	{ // 4.4s
		[0 ... 139] = 4.4
	},
	{ // 5.5s
		[0 ... 139] = 5.5
	},
	{ // 1.1s
		[0 ... 139] = 1.1
	},
	{ // 2.2s
		[0 ... 139] = 2.2
	},
	{ // 3.3s
		[0 ... 139] = 3.3
	}
};


size_t training_data_len = sizeof(training_data) / sizeof(training_data[0]);
