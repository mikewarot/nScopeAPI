all: nscopetest

CC=gcc
CFLAGS+=-I../ -Wall  -g -c
LIBS=libnscope_static.a `pkg-config libusb-1.0 libudev --libs` -lpthread
COBJS=
CPPOBJS= ../nscopetest.o
OBJS=$(COBJS) $(CPPOBJS)

nscopetest: $(OBJS)
	
	g++ -Wall -g $^ $(LIBS) -o nscopetest

$(COBJS): %.o: %.c
	$(CC) $(CFLAGS) $< -o $@

$(CPPOBJS): %.o: %.cpp
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f $(OBJS) nscopetest

.PHONY: clean

.INTERMEDIATE:  $(OBJS)
