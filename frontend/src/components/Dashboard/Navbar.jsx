import React from 'react';
import {
  Box,
  Flex,
  Heading,
  Spacer,
  IconButton,
  useDisclosure,
  Collapse,
  Stack,
} from '@chakra-ui/react';
import { HamburgerIcon, CloseIcon } from '@chakra-ui/icons';

const Navbar = () => {
  const { isOpen, onToggle } = useDisclosure();

  return (
    <Box bg="pink.800" px={4}>
      <Flex h={16} alignItems="center" justifyContent="space-between">
        <Heading color="white"> <img
        src="https://blackcoffer.com/wp-content/uploads/2023/10/Black-720x172-4.png"
        className="h-8"
        alt="BlackCoffer Logo"
        width={200}
      />
 </Heading>
        <Spacer />
        <Flex display={{ base: 'none', md: 'flex' }} alignItems="center" color="white">
          <Stack direction="row" spacing={6}>
            <Box>Home</Box>
            <Box>Dashboard</Box>
            <Box>Analytics</Box>
            <Box>Settings</Box>
          </Stack>
        </Flex>
        <IconButton
          size="md"
          fontSize="lg"
          aria-label="Open Menu"
          color="white"
          onClick={onToggle}
          icon={isOpen ? <CloseIcon /> : <HamburgerIcon />}
          display={{ md: 'none' }}
        />
      </Flex>

      <Collapse in={isOpen} animateOpacity>
        <Box pb={4} display={{ md: 'none' }}>
          <Stack spacing={4} mt={2}>
            <Box>Home</Box>
            <Box>Dashboard</Box>
            <Box>Analytics</Box>
            <Box>Settings</Box>
          </Stack>
        </Box>
      </Collapse>
    </Box>
  );
};

export default Navbar;
